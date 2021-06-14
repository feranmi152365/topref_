from django.db import models

class Faqs(models.Model):
    question = models.CharField(max_length=100 )
    answer = models.CharField(max_length=500 )
    time = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.question
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    