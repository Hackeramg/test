from django.contrib import admin
from .models import Todo
from .models import Gebaeudeerstellen

# Register your models here.

admin.site.register(Todo),

admin.site.register(Gebaeudeerstellen)