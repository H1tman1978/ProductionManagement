# Import Django admin functionality
from django.contrib import admin

# Import Classes from models.py
from .models import LaserMachine, LaserProductionRun, Product

# Register your models here.
admin.site.register(LaserMachine)
admin.site.register(LaserProductionRun)
admin.site.register(Product)
