from django.db import models
from django.contrib.auth.models import User

class product (models.Model):
    brand_name = models.CharField(max_length=100,null=True)
    model_name = models.CharField(max_length=100,null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.brand_name + " " + self.model_name
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    mobile_name = models.CharField(max_length=100,null=True)
    course = models.CharField(max_length=100,null=True)
    fees=models.IntegerField(default=0)

    def __str__(self):
        return self.name