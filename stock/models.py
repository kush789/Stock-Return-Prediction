from django.db import models

class MSFT(models.Model):
	msftid = models.IntegerField()
	value = models.FloatField()
	date = models.DateTimeField()

# class NASDAQ(models.Model):
# 	nasdaqid = models.IntegerField()
# 	value = models.FloatField()
# 	date = models.DateTimeField()

# class DOWJONES(models.Model):
# 	dowjonesid = models.IntegerField()
# 	value = models.FloatField()
# 	date = models.DateTimeField()

# class NIKKEI(models.Model):
# 	nikkeiid = models.IntegerField()
# 	value = models.FloatField()
# 	date = models.DateTimeField()
