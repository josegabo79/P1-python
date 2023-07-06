
#Dockerizar

#Versión de Python desde la cual va a partir este contenedor
FROM python:3.11     

#Crear una carpeta dentro de ese contenedor
WORKDIR /app

#Copiar el archivo que tenemos en  local para pasarlo al enronto al cual vamos a trabajar
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias en el nuevo entorno, sin aplicar el cache y que si hay alguan actualización de gestor de paquetes (requirements)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#Copiar todo nuestro codigo y llevarlo a la carpeta app

COPY . /app

# Encender el contenedor

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]