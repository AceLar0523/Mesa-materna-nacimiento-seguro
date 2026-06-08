const CACHE_NAME = 'mesa-public-sector-v1';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/site.webmanifest',
  '/img/fondo14.avif',
  '/img/logo1.jpg'
];
const QUEUE_DB = 'mesa-panic-alert-queue';
const QUEUE_STORE = 'queued-alerts';

function openQueueDb() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(QUEUE_DB, 1);

    request.onupgradeneeded = () => {
      const database = request.result;
      if (!database.objectStoreNames.contains(QUEUE_STORE)) {
        database.createObjectStore(QUEUE_STORE, { keyPath: 'id', autoIncrement: true });
      }
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function withStore(mode, callback) {
  const database = await openQueueDb();
  return new Promise((resolve, reject) => {
    const transaction = database.transaction(QUEUE_STORE, mode);
    const store = transaction.objectStore(QUEUE_STORE);
    const result = callback(store, resolve, reject);
    transaction.oncomplete = () => resolve(result);
    transaction.onerror = () => reject(transaction.error);
  });
}

async function saveQueuedAlert(payload) {
  await withStore('readwrite', (store) => store.add({ payload, createdAt: new Date().toISOString() }));
}

async function readQueuedAlerts() {
  const database = await openQueueDb();
  return new Promise((resolve, reject) => {
    const transaction = database.transaction(QUEUE_STORE, 'readonly');
    const store = transaction.objectStore(QUEUE_STORE);
    const request = store.getAll();
    request.onsuccess = () => resolve(request.result || []);
    request.onerror = () => reject(request.error);
  });
}

async function clearQueuedAlert(id) {
  await withStore('readwrite', (store) => store.delete(id));
}

async function flushQueuedAlerts() {
  const queuedAlerts = await readQueuedAlerts();

  for (const entry of queuedAlerts) {
    try {
      const response = await fetch('/api/panic-alerts/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(entry.payload)
      });

      if (response.ok) {
        await clearQueuedAlert(entry.id);
      }
    } catch {
      break;
    }
  }
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data.type === 'QUEUE_PANIC_ALERT' && data.payload) {
    event.waitUntil(saveQueuedAlert(data.payload));
  }
});

self.addEventListener('sync', (event) => {
  if (event.tag === 'panic-alert-sync') {
    event.waitUntil(flushQueuedAlerts());
  }
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') {
    return;
  }

  const requestUrl = new URL(event.request.url);
  if (requestUrl.origin !== self.location.origin) {
    return;
  }

  if (requestUrl.pathname.startsWith('/api/')) {
    event.respondWith(
      fetch(event.request).catch(async () => {
        const cached = await caches.match(event.request);
        return cached || Response.error();
      })
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }

      return fetch(event.request)
        .then((networkResponse) => {
          const clone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          return networkResponse;
        })
        .catch(() => caches.match('/index.html'));
    })
  );
});
