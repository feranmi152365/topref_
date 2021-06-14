from django.db import models

class Faqs(models.Model):
    question = models.CharField(max_length=100 )
    answer = models.CharField(max_length=100 )
    time = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.question
    
