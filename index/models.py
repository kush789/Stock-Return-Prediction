from django.db import models

class BSE(models.Model):
	bseid = models.IntegerField()
	value = models.FloatField()
	date = models.DateTimeField()
