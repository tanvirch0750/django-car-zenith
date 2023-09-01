from django.contrib import admin
from .models import Orders

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'car', 'status', 'created_at']
    
admin.site.register(Orders, OrderAdmin)
    
