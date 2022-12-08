from django.db import models

# Create your models here.
class Productos(models.Model):
    id=models.AutoField(primary_key=True)
    produc=models.CharField(max_length=35)
    def __str__ (self):
        return str(self.id)+""+self.produc
    
class Estado(models.Model):
    id=models.AutoField(primary_key=True)
    estado=models.CharField(max_length=25)
    def __str__(self):
        return str(self.id)+""+self.estado
