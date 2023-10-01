from django.db import models

# Create your models here.


class TecDataExcelFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=40)
    file = models.FileField(upload_to="uploads/%Y/%m/%d/")
