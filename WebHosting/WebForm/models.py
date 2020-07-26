from django.db import models


class registrationForm(models.Model):

    FirstName = models.CharField(max_length=20, blank=True, null=True)
    LastName = models.CharField(max_length=20,blank=True,null=True)
    UserName = models.CharField(max_length=20,blank=True,null=True)
    Email = models.CharField(max_length=20,blank=True,null=True)
    Password = models.CharField(max_length=20,blank=True,null=True)
    ConPassword = models.CharField(max_length=20,blank=True,null=True)


class SignupForm(models.Model):

    UserName = models.TextField(max_length=20, blank=True, null=True)
    Email = models.TextField(max_length=20, blank=True, null=True)
    Password = models.TextField(max_length=20, blank=True, null=True)

