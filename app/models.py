from django.db import models
import random
import string
import os
from django.contrib.auth.models import AbstractUser


USER_TYPE = (
    ('Business','Business'),
    ('Computer and Information Technology','Computer and Information Technology'),
    ('Export','Export'),
    ('Government','Government'),
    ('Others','Others')
)


DETECTION_TYPE = (
    ('Single','Single'),
    ('Multiple','Multiple')
)


def file_rename(instance,filename):
    upload_to = 'img'
    name,ext = filename.split('.')
    if instance.pk:
        filename = f"{filename}.{ext}"
    else:
        filename = f"{name}-{''.join(random.choices(string.ascii_lowercase+string.digits,k=8))}.{ext}"
    
    return os.path.join(upload_to,filename)


class UserModel(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email','password']
    full_name = models.CharField(max_length=100,unique=False,null=True,blank=False)
    organisation_name = models.CharField(max_length=100,unique=False,blank=False,null=True)
    organisation_email = models.EmailField(max_length=100,unique=False,blank=False,null=True)
    organisation_strength = models.CharField(max_length=10,blank=True,null=True)
    organisation_type = models.CharField(max_length=50,choices=USER_TYPE)

    def __str__(self):
        return self.username


class UploadData(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    category = models.CharField(max_length=20, null=True, blank=False, unique=False)
    detection_type = models.CharField(max_length=50,choices=DETECTION_TYPE,unique=False, blank=False, null=True)
    filename = models.CharField(max_length=100,unique=False,blank=True,null=True)
    image = models.ImageField(upload_to=file_rename,blank=True,null=True)
    singledetection = models.ImageField(upload_to='singledetection/',blank=True,null=True)
    multidetection = models.ImageField(upload_to='multidetection/',blank=True,null=True)
    count= models.CharField(max_length=10,blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename


class UserProcessCount(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE, null=True)
    totalCount = models.BigIntegerField(unique=False,null=True,blank=True, default=0)
    singleCount = models.BigIntegerField(null=True,blank=True,unique=False,default=0)
    multiCount = models.BigIntegerField(null=True,blank=True,unique=False,default=0)
    
    def __str__(self):
        return str(self.user)
    

class ProductTotalCount(models.Model):
    user = models.ForeignKey(UserModel, null=True, blank=False, on_delete=models.CASCADE)
    item = models.CharField(max_length=50,blank=False,unique=False,null=True)
    totalCount = models.BigIntegerField(null=True, blank=False, default=0,unique=False)
    lastDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
    

class UserCSVRecord(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=False)
    filename = models.CharField(max_length=20,unique=False,null=True,blank=True)
    csvFile = models.FileField(upload_to='reports/',blank=True,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.filename)