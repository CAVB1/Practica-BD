from django.db import models

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=100)
    descrpition = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self) -> str:
        return self.product

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rol = models.CharField(max_length = 100)
    update_date = models.DateTimeField("Fecha de actualizacion")

    def __str__(self) -> str:
        return self.username

class Table(models.Model):
    table = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    def __str__(self) -> str:
        return self.table

class Privilege(models.Model):
    privilege =  models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.privilege

class Control(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    privilege = models.ForeignKey(Privilege, on_delete = models.CASCADE)
    table = models.ForeignKey(Table, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return ", ".join([str(self.user.id) , str(self.privilege.id) , str(self.table.id)])



