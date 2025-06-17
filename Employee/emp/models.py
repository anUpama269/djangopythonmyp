from django.db import models

class Employe(models.Model):
   Name=models.CharField(max_length=50)
   Age=models.IntegerField()
   Salary=models.IntegerField()
   Designation=models.CharField(max_length=50)
   place=models.CharField(max_length=50)
   Image=models.ImageField(upload_to="emp")
   Department_name=models.CharField(max_length=50)


