Pasos a seguir para la creaccion de nuestro proyecto:

Paso 1: Instalacion de lo necesario:

```bash
    # Creaccion del entorno virtual.
    mkvirtualenv pruebaDjango

    # Para actualizar los repositorios.
    python -m pip install --upgrade pip

    # Ejecucion del fichero requirements
    pip install -r requirements.txt
```

Para el fichero requirements.txt pondremos lo siguiente:

```text
    Django~=4.2.7
```

Paso 2: Creaccion de nuestro proyecto:

```bash
    # Para crear los archivos y directorios.
    django-admin startproject mysite .
```

Paso 3: Configuración Básica de nuestro proyecto:
Ahora configuraremos el fichero que esta ubicando en mysite/settings.py y le cambiaremos lo siguinte:

```python
    TIME_ZONE = 'Europe/Madrid'
    LANGUAGE_CODE = 'es-es'
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

Tambien configuraremos la base de datos de nuestro proyecto con lo siguiente en el mismo fichero anterior:

```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Despues de añadir lo de la base de datos tendremos que ejecutar lo siguiente en la terminal:

```bash
    # Para generar el fichero de la base de datos.
    python manage.py migrate
```

Despues de esta configuración ejecutaremos el siguiente comando para probar en el navegador nuestro proyecto en funcionamiento.

```bash
    python manage.py runserver
```

Paso 4: Creacción de Modelo.
