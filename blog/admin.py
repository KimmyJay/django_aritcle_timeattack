import django.contrib.admin
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
