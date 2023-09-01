from django.db import models
from account.models import Account
from car.models import Car

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car.title
