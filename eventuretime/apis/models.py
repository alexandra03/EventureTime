from django.db import models

# Create your models here.
class Uber(models.Model):
    client_id = models.CharField(max_length=60)
    client_secret = models.CharField(max_length=60)
    secret = models.CharField(max_length=60)
    server_token = models.CharField(max_length=60)
