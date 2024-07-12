import sqlite3
from django.db import models, connection

# Create your models here.

class playerModel(models.Model):
	player=models.CharField(max_length=200)
	nation=models.CharField(max_length=200)
	position=models.CharField(max_length=200)
	squad=models.CharField(max_length=200)
	age=models.IntegerField()
	birth_year=models.IntegerField()
	fulltimeplayed=models.FloatField()
	goals=models.IntegerField()
	shots=models.IntegerField()
	sot=models.IntegerField()
	sotpercent=models.FloatField()
	shotspernintey=models.FloatField()
	sotpernintey=models.FloatField()
	goalspershot=models.FloatField()
	goalspersot=models.FloatField()
	shotdistance=models.FloatField()
	xg=models.FloatField() 
	id=models.AutoField(primary_key=True)

	class Meta:
		db_table='playerstats'
		managed = False
	def __str__(self):
		return self.player
