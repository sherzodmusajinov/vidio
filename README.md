# step-1
```commandline
    django-admin startproject book .
```
# step-2
```commandline
    django-admin startapp blog
```
# step-3
```commandline
INSTALLED_APPS = [
    ...
    'blog',
]
```

# step-4
create folder templates
```commandline
 mkdir blog/tempates
```

# step-5
create file index.html
```commandline
touch templates/index.html
```

# step-6
create file blog/urls.py
* blog/urls.py
```commandline
from django.urls import path
from .views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
```

# step-7
* book/urls.py
```commandline
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

```

# step-8
```commandline
python manage.py migrate
```

# step-9
```commandline
python manage.py runserver
```


# step-10
create models
```commandline
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    
    def __str__(self):
    return f"{self.title}"

```

# step-11
*blog/admin.py
```commandline
from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
```

# step-12
```commandline
python manage.py makemigrations
python manage.py migrate
```

# step-13
```commandline
python manage.py createsuperuser
```