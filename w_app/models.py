from django.db import models

# Create your models here.
class signupModel(models.Model):
    created = models.DateTimeField(auto_now_add =  True)

    firstname = models.CharField(max_length = 29)
    lastname = models.CharField(max_length = 29)
    username = models.EmailField()
    password = models.CharField(max_length = 29)
    city = models.CharField(max_length = 29)
    state = models.CharField(max_length = 29)
    mobile = models.BigIntegerField()

class notesModel(models.Model):
    created = models.DateTimeField(auto_now_add =  True)

    title = models.CharField(max_length = 2912)
    cate = models.CharField(max_length = 2912)
    myfile = models.FileField(upload_to='Notes_File')
    dsc = models.TextField()

class feedbackModel(models.Model):
    created = models.DateTimeField(auto_now_add =  True)

    name = models.CharField(max_length = 2912)
    subject = models.CharField(max_length = 2912)
    email = models.EmailField()
    message = models.TextField()