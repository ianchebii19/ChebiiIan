from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)  # Fixed missing argument for primary_key
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
