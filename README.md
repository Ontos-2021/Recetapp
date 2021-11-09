# Recetapp
¡Hola! ¡Bienvenido/a a Recetapp!

Recetapp es una aplicación web basada en Django para poder gestionar tus recetas

El proyecto aún está en desarrollo, sin embargo puedes ver cómo va quedando :)

## ¿Que hay que hacer para correr el proyecto?

- Primero tienes que clonar el repositorio

    ``` > git clone https://github.com/Ontos-2021/Recetapp.git ```


- Después tienes que ingresar a la carpeta, crear un entorno virtual de python y descargar Django.
    ```
  > cd Recetapp
  > 
  > python -m venv env
  > 
  > env\Scripts\activate (Windows)
  > 
  > (env) pip install django
  ```

- Finalmente puedes iniciar el proyecto con el siguiente comando
` > python manage.py runserver `

### También puedes crear un superusuario.

Creando un superusuario puedes gestionar la base de datos desde el sitio de administrador de Django.
Ingresa este comando y luego ingresas un usuario, contraseña y un e-mail de recuperación.

` > python manage.py createsuperuser `

---

## Modelo de la base de datos

El modelo está hecho con [Mysql Workbench](Recetapp.mwb "Archivo MySql Workbench")

![Modelo de la base de datos hecha en MySql Workbench](Recetapp%20(Modelo).png "Modelo") 
