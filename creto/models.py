from django.db import models

# Create your models here.

class Creto(models.Model):

	title = models.CharField(default='best bikes for you', max_length=50)
	# numero de telephone 1
	telephone = models.CharField(default='99999999', max_length=8)
	# numero de telephone 2
	telephone2 = models.CharField(default='99999999', max_length=8)

	email = models.CharField(default='creto@gmail.com', max_length=50)


	email2 = models.CharField(default='rovadex@gmail.com', max_length=50)

	address = models.CharField(max_length=255, default='Rovadex © 2020. All Rights Reserved')

	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Creto"
		verbose_name_plural = "Creto Informations"

	def __str__(self):
		return self.title
