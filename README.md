# jetDjango

<h2 align="center">JET</h2>
<h3 align="center">Proyecto UVG Cifrado de Información</h3>
<h3 align="left">Este repositorio contiene la parte de Django necesaria para el funcionamiento de JET</h3>

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
* Crear archivo /tutos/credentials.py
    ```python
    DEVELOPMENT_DATABASE = {
        'NAME': 'jet_db',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-contraseña',
        'HOST': 'tu-host',
        'PORT': 'tu-puerto',
    }
    ```
