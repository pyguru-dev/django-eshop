from django.db import models

class ContactSubject(models.Model):
    title = models.CharField(max_length=100)
   

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name + ' : ' +self.email


class FaqGroup(models.Model):
    title = models.CharField(max_length=100)
    

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer   = models.CharField(max_length=255)
    
    
    