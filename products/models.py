from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'categories'
	def __str__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	category = models.ForeignKey(Category)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'products'

	def __str__(self):
		return self.title