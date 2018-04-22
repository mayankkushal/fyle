from django.db import models

# Create your models here.

class Bank(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Branch(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True, editable=False)
	bank = models.ForeignKey('bank', on_delete=models.CASCADE)
	branch = models.CharField(max_length=200)
	address = models.TextField()
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)

	def __str__(self):
		return self.branch