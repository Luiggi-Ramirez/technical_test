# usamos una imagen de python 3.12
FROM python:3.12-slim

# asignamos el esapcio de trabajo dentro del container
WORKDIR /app
# copiamos toda la app dentro del espacio de trabajo de tranajo del container excepto lo que este en el .dockerignore
COPY . /app/

# instalamos las dependencias sin dejar cache
RUN pip install --no-cache-dir -r requirements.txt

# exponemos el puerto por defecto
EXPOSE 8000

# ejecutamos el server
CMD ["uvicorn", "todo_list.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
