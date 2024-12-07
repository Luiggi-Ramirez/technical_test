# Prueba tecnica
Objetivos:

1. Implementar una API con endpoints básicos (CRUD). ✔
2. Utilizar buenas prácticas de programación (estructura de código, manejo de errores, etc.). ✔
3. Implementar testing unitario y de integración utilizando pytest . ✔
4. Configurar linters (como flake8 o pylint ) y herramientas de formateo (como black ). ✔
5. Configurar y levantar la aplicación en un contenedor Docker. ✔
6. Incluir un archivo README.md con las instrucciones para levantar la aplicación y ejecutar las pruebas. ✔
7. Bonus: Cambiar el alcance de RestAPI a GraphQL con Strawberry. ✔

# Todo List API

API para crear, listar, actualizar y eliminar tareas.

# Requisitos del sistema

Python 3.12

Docker

# Antes de ejecutar
Clonar repo:

   `git clone https://github.com/Luiggi-Ramirez/technical_test.git`

# Ejecutar en local

1. Crear un entorno virtual:

   `python -m venv env`

2. Ingresar al entorno virtual:

   windows

   `.\env\Scripts\activate`

   linux

   `source env/bin/activate`

3. Instalar las dependencias del proyecto:

   `pip install -r requirements.txt`

4. Ejecutar el proyecto:

   `uvicorn todo_list.main:app --reload`

# Linter

Para ejecutar el linter flake8:

`flake8 -v`

# Formatter

Para black uso generalmente el de la extensión de vsc.
Para ejecutar black formatter:

`black .`

# Pruebas

Para ejecutar los test unitarios y de integración:

   `pytest`

# Ejecutar en docker

En la misma carpeta en la que esta el docker-compose se ejecuta el sgte. command:

   `docker compose  up --build -d`

# Linter en docker

Para ejecutar el linter flake8 dentro de docker:

   `docker exec todolist_api flake8 -v`

# Formatter en docker

Para ejecutar black formatter dentro de docker:

   `docker exec todolist_api black .`

# Pruebas en docker

Para ejecutar los test unitarios y de integración dentro de docker:

   `docker exec todolist_api pytest`

# Documentación
Sea en local o en docker se ingresa con la sgte. ruta:
   `http://127.0.0.1:8000/docs`

# Graphql
Sea en local o en docker se ingresa con la sgte. ruta:
   `http://127.0.0.1:8000/graphql`

## Querys y mutations de ejemplo
### Obtener todas las tareas
   `query GetTasks{
      tasks{
         id
         title
         description
         completed
      }
   }
   `
### Obtener detalle de tarea por id
   `query GetTaskById{
      task(id:4){
         id
         title
         description
         completed
      }
   }
   `
### Crear nueva tarea
   `mutation CreateTask{
      createTask (
      input: {
         id: 4, 
         title: "Tarea 4", 
         description: "Tarea 4", 
         completed: false
      }
      ){
         id
         title
         description
         completed
      }
   }
   `
### Actualizar tarea por id
   `mutation UpdateTask{
      updateTask (
      id:4
      input: {
         title: "Tarea 4", 
         description: "Tarea 4", 
         completed: true
      }
      ){
         id
         title
         description
         completed
      }
   }
   `
### Eliminar tarea
   `mutation DeleteTask{
      deleteTask(id: 1)
   }
   `

