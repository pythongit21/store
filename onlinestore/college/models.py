from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Order_material(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return self.order
