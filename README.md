# Mesa de Maternidad y Nacimiento Seguro

![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

Una plataforma integral para la gestión y seguimiento de casos de maternidad y nacimiento seguro, desarrollada con tecnologías modernas y con enfoque en la excelencia clínica y la seguridad de la madre y el recién nacido.

## 🎯 Descripción del Proyecto

La **Mesa de Maternidad y Nacimiento Seguro** es una aplicación web que facilita:

- ✅ Gestión integral de casos de maternidad
- ✅ Seguimiento del estado de embarazo y nacimiento
- ✅ Registro de atenciones y procedimientos clínicos
- ✅ Análisis de indicadores de seguridad materna
- ✅ Generación de reportes y estadísticas
- ✅ Coordinación entre equipos multidisciplinarios

## 🛠️ Stack Tecnológico

### Frontend
- **Vue.js 3** - Framework progresivo para interfaces de usuario
- **TypeScript** - Tipado estático para mayor seguridad
- **Vite** - Build tool y dev server ultra rápido
- **GSAP** - Animaciones smoothas y profesionales
- **Lenis** - Smooth scrolling
- **PrimeUIX** - Componentes de UI modernos
- **Three.js** - Visualización 3D interactiva

### Backend
- **Python 3.x** - Lenguaje de programación
- **Django 6.0.3** - Framework web robusto
- **Django REST Framework** - API RESTful
- **PostgreSQL** - Base de datos relacional

### DevOps & Herramientas
- **Node.js/npm** - Gestor de dependencias frontend
- **Pip** - Gestor de dependencias Python
- **ESLint** - Linting de código
- **Prettier** - Formateador de código
- **Husky** - Git hooks

## 📋 Requisitos Previos

### Sistema
- Git
- Node.js v16+ y npm
- Python 3.8+
- PostgreSQL 12+

### Instalación de PostgreSQL (si no lo tienes)
```bash
# Windows (usando chocolatey)
choco install postgresql

# macOS (usando brew)
brew install postgresql@15

# Linux (Ubuntu/Debian)
sudo apt-get install postgresql postgresql-contrib
```

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_REPOSITORIO>
cd unicefproyect
```

### 2. Configurar Backend (Django)

```bash
# Entrar en la carpeta backend
cd backend

# Crear entorno virtual (Windows)
python -m venv venv
venv\Scripts\activate

# Crear entorno virtual (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones (DB, SECRET_KEY, etc.)

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (admin)
python manage.py createsuperuser

# Iniciar servidor de desarrollo
python manage.py runserver
```

**El backend estará disponible en:** `http://localhost:8000`

### 3. Configurar Frontend (Vue.js)

```bash
# Volver a la raíz y entrar en frontend
cd ../frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

**El frontend estará disponible en:** `http://localhost:5173`

## 🚀 Uso y Desarrollo

### Frontend - Comandos útiles

```bash
cd frontend

# Desarrollo con recargate en caliente
npm run dev

# Construir para producción
npm run build

# Previsualizar build de producción
npm run preview

# Verificar tipos TypeScript
npm run type-check

# Lint y fix de código
npm run lint

# Formatear código
npm run format

# Crear nuevo componente
npm run new:component
```

### Backend - Comandos útiles

```bash
cd backend

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear datos de prueba
python manage.py seed  # (si existe script de seed)

# Shell interactivo Django
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic

# Tests
python manage.py test
```

## 📂 Estructura del Proyecto

```
unicefproyect/
├── frontend/                 # Aplicación Vue.js 3
│   ├── src/
│   │   ├── components/      # Componentes reutilizables
│   │   ├── pages/           # Páginas de la aplicación
│   │   ├── composables/     # Vue 3 Composables
│   │   ├── views/           # Vistas principales
│   │   ├── router/          # Configuración de rutas
│   │   ├── stores/          # Estado global (Pinia)
│   │   ├── types/           # Tipos TypeScript
│   │   ├── assets/          # Imágenes, fuentes, etc.
│   │   ├── css/             # Estilos globales
│   │   ├── App.vue          # Componente raíz
│   │   └── main.ts          # Punto de entrada
│   ├── public/              # Archivos estáticos
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── eslint.config.ts
│
├── backend/                  # Aplicación Django
│   ├── api/                 # App principal de API
│   │   ├── models.py        # Modelos de datos
│   │   ├── views.py         # Vistas y endpoints
│   │   ├── serializers.py   # Serializadores DRF
│   │   ├── urls.py          # Rutas de API
│   │   ├── admin.py         # Admin de Django
│   │   └── migrations/      # Migraciones de BD
│   ├── core/                # Configuración principal
│   │   ├── settings.py      # Configuraciones

│   │   ├── urls.py          # URLs raíz
│   │   ├── wsgi.py          # Configuración WSGI
│   │   └── asgi.py          # Configuración ASGI
│   ├── manage.py
│   ├── requirements.txt     # Dependencias Python
│   └── .env.example         # Variables de entorno
│
└── README.md                # Este archivo
```

## 🔌 API Endpoints

### Autenticación
```
POST   /api/auth/login/
POST   /api/auth/logout/
POST   /api/auth/register/
```

### Gestión de Casos
```
GET    /api/cases/             # Listar todos los casos
POST   /api/cases/             # Crear nuevo caso
GET    /api/cases/{id}/        # Obtener detalle de caso
PUT    /api/cases/{id}/        # Actualizar caso
DELETE /api/cases/{id}/        # Eliminar caso
```

### Reportes
```
GET    /api/reports/           # Listar reportes
POST   /api/reports/           # Generar nuevo reporte
GET    /api/reports/{id}/      # Descargar reporte
```

## 🔒 Variables de Entorno

### Backend (.env)
```env
# Django
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Base de Datos
DB_ENGINE=django.db.backends.postgresql
DB_NAME=maternidad_db
DB_USER=postgres
DB_PASSWORD=tu-contraseña
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend (.env.local)
```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=Mesa de Maternidad y Nacimiento Seguro
```

## 📊 Base de Datos

### Crear base de datos PostgreSQL

```bash
# Conectarse a PostgreSQL
psql -U postgres

# Crear base de datos
CREATE DATABASE maternidad_db;

# Crear usuario
CREATE USER maternidad_user WITH PASSWORD 'tu_contraseña';

# Dar permisos
ALTER ROLE maternidad_user SET client_encoding TO 'utf8';
ALTER ROLE maternidad_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE maternidad_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE maternidad_db TO maternidad_user;

# Salir
\q
```

## 🧪 Testing

### Frontend
```bash
cd frontend
npm run test
```

### Backend
```bash
cd backend
python manage.py test
```

## 📈 Despliegue

### Producción - Backend (Django)
```bash
# Actualizar settings.py para producción
DEBUG = False
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']

# Recolectar estáticos
python manage.py collectstatic --noinput

# Usar gunicorn como servidor
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

### Producción - Frontend (Vue.js)
```bash
cd frontend
npm run build
# Los archivos compilados estarán en dist/
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👥 Autores y Contribuidores

- **Equipo de Desarrollo** - Desarrollo inicial y mantenimiento

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, contacta a:
- Email: [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)
- Issues del proyecto: [GitHub Issues](https://github.com/tu-usuario/proyecto/issues)

## 🙏 Agradecimientos

Agradecemos a todos aquellos que han contribuido al desarrollo de esta plataforma dedicada a mejorar la seguridad materna.

---

**Última actualización:** Abril 2026
