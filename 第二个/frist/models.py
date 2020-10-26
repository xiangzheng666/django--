from django.db import models

# Create your models here.
class  my_data(models.Model):
	name=models.CharField(max_length=20)
	number=models.CharField(max_length=20)
	address=models.CharField(max_length=20)
