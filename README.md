# Recetapp
¡Hola! ¡Bienvenido/a a Recetapp!

Recetapp es una aplicación web basada en Django para poder gestionar tus recetas

El proyecto aún está en desarrollo, sin embargo puedes ver cómo va quedando :)

## ¿Que hay que hacer para correr el proyecto?

- Primero tienes que ir a una carpeta donde quieras que esté el proyecto
- Abrir la terminal 
- Clonar el repositorio con el siguiente comando (para este paso debes tener [Git](https://git-scm.com/downloads "Descargar Git") instalado en tu computador)

  `git clone https://github.com/Ontos-2021/Recetapp.git`
  - Si no puedes simplemente descargar el [ZIP](https://github.com/Ontos-2021/Recetapp/archive/refs/heads/main.zip "Descargar Zip")
- Después tienes que ingresar a la carpeta del proyecto

  `cd Recetapp`
- Crear un entorno virtual de python

  `python -m venv env`
- Activar el entorno virtual
  
  `env\Scripts\activate (Windows)`
- Descargar Django

  `(env)> pip install django`
- Finalmente puedes iniciar el proyecto con el siguiente comando `python manage.py runserver`

### También puedes crear un superusuario.

Creando un superusuario puedes gestionar la base de datos desde el sitio de administrador de Django.
Ingresa este comando y luego ingresas un usuario, contraseña y un e-mail de recuperación.

`python manage.py createsuperuser`

---

## Modelo de la base de datos

- El modelo está hecho con [Mysql Workbench](Recetapp.mwb "Archivo MySql Workbench")

- El modelo en el proyecto de django está representado en el archivo [```models.py```](Recetapp/Apps/Recetas/models.py "Modelo en el proyecto")

![Modelo de la base de datos hecha en MySql Workbench](Recetapp%20(Modelo).png "Modelo") 

