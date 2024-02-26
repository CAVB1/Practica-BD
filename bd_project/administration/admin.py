from django.contrib import admin
from .models import User, Privilege, Product, Table, Control

# Register your models here.

admin.site.register(User)
admin.site.register(Privilege)
admin.site.register(Product)
admin.site.register(Table)
admin.site.register(Control)