from django.db import models

# Create your models here.
class userdb(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    image = image = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    lname = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    def str(self):
        return self.name


class logindb(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    def str(self):
        return self.name
