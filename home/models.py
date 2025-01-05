from django.db import models

class Register(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    age=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    position=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + self.last_name

