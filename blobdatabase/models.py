from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
    
class Building(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    

class Blob(models.Model):
    name = models.CharField(max_length=200)
    fullPath = models.CharField(max_length=400)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    modifiedDate = models.DateTimeField('date modified')
    createdDate = models.DateTimeField('date created')
    modifiedBy = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)
    extension = models.CharField(max_length=30)
    def __str__(self):
        return self.name 
    