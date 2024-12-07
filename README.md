# Todo List API

API para crear, listar, actualizar y eliminar tareas.

# Requisitos del sistema

Python 3.12+
Docker

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

Hay que estar al nivel del docker-compose
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
