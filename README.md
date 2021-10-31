# Recetapp
¡Hola! ¡Bienvenido/a a Recetapp!

Recetapp es una aplicación web basada en Django para poder gestionar tus recetas

El proyecto aún está en desarrollo, sin embargo puedes ver cómo va quedando :)

# ¿Que hay que hacer para correr el proyecto?

Tienes que ingresar a la carpeta, crear un entorno virtual de python y descargar Django.

> cd Recetapp
> 
> python -m venv env
> 
> env\Scripts\activate (Windows)
> 
> (env) pip install django
 
Luego puedes iniciar el proyecto con el siguiente comando

> python manage.py runserver

# También puedes crear un superusuario.

Así puedes gestionar la base de datos desde el sitio de administrador.
Ingresa este comando y luego ingresas un usuario, contraseña y un e-mail de recuperación.

> python manage.py createsuperuser

¡Eso es todo, que lo disfrutes!
