from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=64)
    start_time = models.DateTimeField(verbose_name='start_time')
    end_time = models.DateTimeField(verbose_name='end_time')
    s_code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)],
                                              verbose_name="s_code", unique=True)
    price = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)],
                                             verbose_name="price")

    def __str__(self):
        return f"{self.name}  {self.price}-Lari"


class Order(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='first_name')
    last_name = models.CharField(max_length=64, verbose_name='last_name')
    ticket = models.OneToOneField('ecommerce.Ticket', on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return f"{self.last_name}  {self.first_name}"
