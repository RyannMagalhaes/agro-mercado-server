from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)]) # Garante que o nome do produto tenha no mínimo 3 caracteres e no máximo 20
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    
    