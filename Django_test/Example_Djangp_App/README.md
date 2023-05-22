Primeros pasos:
# Aquí pondremos las instrucciones para poder ejecutar nuestra aplicación
Crear el intorno virtual: virtualenv <Nombre del entorno>
Activar el entorno: source /env/bin/activate
Cerrar el entorno: deactivate
Borrar el entorno virtual: rm -rf <nombre entorno>
Crear un archivo requeriments.txt --> pip freeze > requeriments.txt
Para arrancar el proyecto: python manage.py runserver 8000
Hace las migraciones: python manage.py makemigrations <nombre de la app> 
                                       migrate <nombre de la app>
Crear un superusuario: python manage.py createsuperuser
Instrucción para crear archivo de traducción: django-admin makemessages -l es
Instrucción compilar la traducción: Anchura de sépalo en cm: