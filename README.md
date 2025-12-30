# tasks_app

## Descripción

Esta API implementa un sistema básico de tareas (Tasks), con autenticación JWT, CRUD completo y listado paginado.
El objetivo es demostrar capacidad de construir una API funcional, segura y mantenible usando FastAPI, SQLAlchemy y PostgreSQL.

## Tecnologías utilizadas

- Python 3.11

- FastAPI

- SQLAlchemy

- PostgreSQL (Docker)

- Alembic (migraciones)

- JWT para autenticación

- Passlib (bcrypt) para hashing de contraseñas

- Pydantic para validación de datos

## Configuración  


### Instalación  

Creación del ambiente virtual  
python3.11 -m venv venv  

Activación del ambiente virtual  
source venv/bin/activate  # Linux / Mac  
venv\Scripts\activate     # Windows  
source venv/scripts/activate  # Con git bash en Windows  

Instalación de los requerimientos de la apliación  
pip install -r requirements.txt  

### Variables de entorno  

Para esto se debe crear un archivo .env en la carpeta raiz del proyecto o sea la ruta "tasks_app/", el archivo debe tener esta configuración:  

POSTGRES_DB=task_manager_db  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
POSTGRES_PORT=5433  
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/task_manager_db  
SECRET_KEY=5bae3c3872d72ec58dc9899ad111436d580b146e591ee8bfa0727a22e8f292f7  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=30  

### Creación de la Base de datos  

En la ruta "tasks_app/", ejecutar el comando: docker-compose up -d  

Asegurarse de que Docker se esté ejecutando  

### Migraciones

Creación de las migraciones y usuario inicial  
alembic upgrade head  

Esto creará las tablas y el usuario para pruebas:  
email: admin@test.com  
password: admin123  

## Ejemplos de uso en Postman  

1. Signup  

Método: POST

URL: http://localhost:8000/api/users/register

Body (raw, JSON):

{
  "username": "testuser",
  "email": "user@example.com",
  "password": "passwordtest"
}


Respuesta esperada:

{
  "id": 1,
  "username": "testuser",
  "email": "user@example.com",
  "is_active": true
}

2. Login  

Método: POST

URL: http://localhost:8000/api/auth/login

Body (raw, JSON):

{
  "email": "admin@example.com",
  "password": "admin123"
}


Respuesta esperada:

{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}


Nota: Copia el valor de access_token para los siguientes endpoints.

3. Crear una tarea, por defecto se crea con el status="pending" y en total existen 3 estados: "pending", "in_progress", "done".

Método: POST

URL: http://localhost:8000/api/task/create_task

Headers:

Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json


Body (raw, JSON):

{
  "title": "Nueva tarea",
  "description": "Descripción de ejemplo",
  "status": "pending"
}


Respuesta esperada:  

{
  "title": "Nueva tarea",  
  "description": "Descripción de ejemplo",  
  "status": "pending",  
  "id": 0,  
  "created_at": "2025-12-30T04:12:33.678Z",  
  "updated_at": "2025-12-30T04:12:33.678Z",  
  "created_by": 0  
}

4. Listado de tareas con paginación  

Método: GET  

URL: http://localhost:8000/api/task/my_tasks?page=1&page_size=5  

Headers:  

Authorization: Bearer <JWT_TOKEN>  


Respuesta esperada:  

{  "total": 15,  
  "page": 2,  
  "page_size": 10,  
  "data": [  
  {  
    "id": 1,  
    "title": "Nueva tarea",  
    "description": "Descripción de ejemplo",  
    "status": "pending",  
    "created_at": "2025-12-29T12:00:00Z",  
    "updated_at": "2025-12-29T12:00:00Z",  
    "created_by": 0  
  },  
  ...  
  ]  
}

5. Obtener una tarea por ID  

Método: GET  

URL: http://localhost:8000/api/task/1  

Headers:  

Authorization: Bearer <JWT_TOKEN>  


Respuesta esperada:  

{  
    "id": 1,  
    "title": "Nueva tarea",  
    "description": "Descripción de ejemplo",  
    "status": "pending",  
    "created_at": "2025-12-29T12:00:00Z",  
    "updated_at": "2025-12-29T12:00:00Z",  
    "created_by": 0  
}  

6. Actualizar una tarea  

Método: PUT  

URL: http://localhost:8000/api/task/update/1  

Headers:  

Authorization: Bearer <JWT_TOKEN>  
Content-Type: application/json  


Body (raw, JSON): Solo los campos a modificar  

{
  "title": "Tarea actualizada",  
  "status": "done"  
}


Respuesta esperada:  

{  
  "title": "Tarea actualizada",  
  "description": "string",  
  "status": "done",  
  "id": 0,  
  "created_at": "2025-12-30T04:18:32.563Z",  
  "updated_at": "2025-12-31T04:18:32.563Z",  
  "created_by": 0  
}

7. Eliminar una tarea  

Método: DELETE  

URL: http://localhost:8000/api/task/delete/1  

Headers:  

Authorization: Bearer <JWT_TOKEN>  


Respuesta esperada:  

{  
  "message": "Task deleted successfully"  
}