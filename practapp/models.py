from django.db import models

# Create your models here.
class Division(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Discrict(models.Model):
    division=models.ForeignKey(Division,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class PersonalInfo(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField(max_length=250,default=0)
    email=models.EmailField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name=models.CharField(max_length=250)
  
    def __str__(self):
        return self.name

class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    

    def __str__(self):
        return self.name

class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name









