from django.db import models

# Create your models here.

class message(models.Model):
	text = models.TextField(max_length=800)
	def __str__(self):
		return self.text
    