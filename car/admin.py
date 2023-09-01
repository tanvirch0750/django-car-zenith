from django.contrib import admin
from . import models

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'color', 'brand', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(models.Car, CarAdmin)
