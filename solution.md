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
Para la creación de nuestra aplicacion de tarea ejecutaremos lo siguiente en la terminal:
```bash
    # Para la creacion de nuestra aplicacion de tarea.
    python manage.py startapp task
```

Despues configuraremos lo siguiente en el fichero mysite/settings.py

```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```

Ahora configuraremos el fichero de modelo en la carpeta de task. Que lo que pondremos en ese fichero sera lo siguiente:
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

Despues de añadir en fichero lo anterior tendremos que ejecutar lo siguiente en la terminal:

```bash
    # Para preparar los ficheros para migrarlo a la base de datos.
    python manage.py makemigrations task

    # Django preparó un archivo de migración que ahora tenemos que aplicar a nuestra base de datos.
    python manage.py migrate task
```
Paso 5: Administracción de Django.
Abre el fichero task/admin.py en el editor y reemplaza su contenido con esto:
```python
    from django.contrib import admin
    from .models import Task

    admin.site.register(Task)
```

Despues de añadir lo anterior en el fichero indicado tendremos que ejecutar lo siguiente en la terminal:
```bash
    # Creaccion del usuario.
    python manage.py createsuperuser
```

Paso 6: Configuración de las Urls.
Para la configuración de las urls de nuestro proyecto tendremos que modificar lo siguiente:
```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('task.urls')),
    ]
```

Crea un nuevo fichero vacío llamado urls.py en el directorio task para añadir lo siguiente en el fichero:
```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.task_list, name='task_list'),
    ]
```

Paso 7: Creacción de las vistas.
Ahora configuraremos el fichero views.py de la carpeta task que pondremos lo siguiete:
```python
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
```

Paso 8: Creacción de plantillas.
Ahora crearemos en la carpeta de task un nuevo directorio llamado templates y dentro de ella crearemos otra carpeta llamada tasks.
Dentro de esta carpeta crearemos nuestra primera plantilla con el siguiente nombre task_list.html, dentro del fichero pondremos lo siguiente:

