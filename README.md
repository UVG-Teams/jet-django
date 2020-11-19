# jetDjango

<h2 align="center">JET</h2>
<h3 align="center">Proyecto UVG Cifrado de Información</h3>

## Configuración de entorno

* [Instalar Python](https://www.python.org/)
* [Instalar Postgres](https://www.postgresql.org/)
* Instalar Python Environment
    ```shell
    $ sudo apt install python3-env
    ```
* Clonar repo
* Crear, activar python env
    ```shell
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
* Instalar dependencias (dentro de la carpeta /tutos/)
    ```shell
    $ pip install -r requirements.txt
    ```
* [Si necesita ayuda para instalar psycopg2](https://www.psycopg.org/)

## Configuración de Base de Datos
* Crear archivo /jet/credentials.py
    ```python
    DEVELOPMENT_DATABASE = {
        'NAME': 'jet_db',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-contraseña',
        'HOST': 'tu-host',
        'PORT': 'tu-puerto',
    }
    ```
* Crear/resetear db y correr migrations
    ```shell
    $ python load_data.py
    ```

## Desarrollo

* Run Server
    ```shell
    $ python manage.py runserver
    ```
