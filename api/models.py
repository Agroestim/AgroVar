from django.db import models

# Create your models here.

# TODO: Definir los modelos segun la estructura de los ficheros de
# datos del INTA.


class TechnicalDataFileModel(models.Model):
    file_id = models.AutoField(max_digits=10)
    gridfs_id = models.CharField(max_length=30, blank=True)
    file_name = models.CharField(max_length=40)


class TechnicalDataModel(models.Model):
    ...
