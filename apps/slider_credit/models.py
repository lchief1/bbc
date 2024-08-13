from apps.shared.models import AbstractBaseModel
from django.db import models

class Slider(AbstractBaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slides/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Credit(AbstractBaseModel):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount}"



