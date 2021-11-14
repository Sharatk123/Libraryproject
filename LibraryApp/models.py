from django.db import models

# Create your models here.

class AddBook(models.Model):
    title=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    cost=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    file=models.FileField(upload_to="blogs/",null=True,blank=True)

    def __str__(self):
        return self.title

class SignUp(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SignIn(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.username