from django.db import models

# Create your models here.
class Register(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=255)
    uemail=models.EmailField()
    unumber=models.IntegerField()
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.uname 