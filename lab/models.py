from django.db import models

class Person(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    name= models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1,choices=SEX)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctor_name= models.CharField(max_length=30)

class Test(models.Model):
    test_name=models.CharField(max_length=50)
    test_result=models.CharField(max_length=50,null=True)
    test_normalvalue=models.CharField(max_length=50,null=True)
    


    
