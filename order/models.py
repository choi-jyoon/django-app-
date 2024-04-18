from django.db import models
from django.contrib.auth.models import User
from seller.models import Food

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    
    