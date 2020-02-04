from django.db import models

# Create your models here.

class Teapot_Message(models.Model):
    teapot_quote = models.TextField()
