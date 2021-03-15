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
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f"{filename}.{ext}"
    else:
        filename = f"{''.join(random.choices(string.ascii_letters+string.digits,k=10))}.{ext}"
    
    return os.path.join(upload_to,filename)


class Reports(models.Model):
    filename = models.CharField(max_length=20,unique=False,null=True,blank=True)
    report = models.FileField(upload_to='reports/',blank=True,null=True)

    def __str__(self):
        return self.filename


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


class UserRecordCount(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE, null=True)
    totalCount = models.BigIntegerField(unique=False,null=True,blank=True, default=0)
    singleCount = models.BigIntegerField(null=True,blank=True,unique=False,default=0)
    multiCount = models.BigIntegerField(null=True,blank=True,unique=False,default=0)
    
    def __str__(self):
        return str(self.user)