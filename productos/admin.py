from django.contrib import admin
from .models import Productos

@admin.register(Productos)
class AuthorAdmin(admin.ModelAdmin):
    pass
