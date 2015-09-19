from django.db import models

# Create your models here.

class Instagram(models.Model):
	client_id = models.CharField(max_length=60)


class Yelp(models.Model):
	token = models.CharField(max_length=60)
	token_secret = models.CharField(max_length=60)
	consumer_key = models.CharField(max_length=60)
	consumer_secret = models.CharField(max_length=60)