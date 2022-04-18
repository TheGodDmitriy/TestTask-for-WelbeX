from django.db import models

#Инициализация таблицы
class Table(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=500)
    Amount = models.CharField(max_length=500)
    Distance = models.CharField(max_length=500)
