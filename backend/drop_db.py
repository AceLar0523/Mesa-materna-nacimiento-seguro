import psycopg2

try:
    conn = psycopg2.connect('dbname=postgres user=postgres password=admin host=localhost')
    conn.autocommit = True
    cur = conn.cursor()
    
    # Terminar otras conexiones
    cur.execute("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'mesamaternadb' AND pid <> pg_backend_pid()")
    
    # Dropear la BD
    cur.execute('DROP DATABASE IF EXISTS mesamaternadb')
    cur.execute('CREATE DATABASE mesamaternadb')
    
    conn.close()
    print('✓ Database reset successfully')
except Exception as e:
    print(f'Error: {e}')
