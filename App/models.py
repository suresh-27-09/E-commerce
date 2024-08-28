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
class Category(models.Model):
    cid=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.c_name
class Products(models.Model):
    pid=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=255)
    p_price=models.FloatField()
    p_img=models.ImageField(upload_to='images/')
    p_des=models.TextField()

    def __str__(self):
        return self.p_name

