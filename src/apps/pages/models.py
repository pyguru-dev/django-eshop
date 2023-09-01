from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name + ' : ' +self.email
