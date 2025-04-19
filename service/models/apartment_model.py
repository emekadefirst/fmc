from django.db import models
from utils.base_model import BaseModel


class ApartmentType(BaseModel):
    name = models.CharField(max_length=55)
    number_of_room = models.PositiveIntegerField(default=0)
    number_of_bathroom = models.PositiveIntegerField(default=0)
    in_kitchen = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def save(self, *args, **kwargs): 
        if not self.in_kitchen:
            self.number_of_room += 1
            self.number_of_bathroom += 1
        return super().save(*args, **kwargs)


class ExtraSpace(BaseModel):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name