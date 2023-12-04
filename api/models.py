from django.db import models

from api.models_choices import (
    DEFAULT_CHOICE_VALUE,
    LOCATIONS_CHOICES,
    PAPER_TYPES_CHOICES,
    REFERENCES_CHOICES,
    VARITIES_CHOICES,
)

# Create your models here.


class CampaignPaperFileModel(models.Model):
    file_id = models.AutoField(primary_key=True)
    gridfs_id = models.CharField(max_length=30, blank=True)
    file_name = models.CharField(max_length=40)


class VarietyPaperModel(models.Model):
    paper_id = models.BigAutoField(primary_key=True)
    variety = models.CharField(
        verbose_name="Variedad", choices=VARITIES_CHOICES, max_length=50, null=False
    )
    humidity_percentage = models.FloatField(verbose_name="Humedad", blank=False)
    performance = models.IntegerField(verbose_name="Redimiento (kg/ha)", blank=False)
    relative_performance = models.IntegerField(
        verbose_name="Redimiento Relativo", blank=False
    )
    grains_count = models.IntegerField(verbose_name="Numero de granos", blank=False)
    grains_per_spike = models.IntegerField(
        verbose_name="Granos por espiga", blank=False
    )
    weight_per_thousand_grains = models.FloatField(
        verbose_name="Peso por mil granos", blank=False
    )
    proteins_percentage = models.FloatField(verbose_name="Proteinas", blank=False)
    ph = models.FloatField(verbose_name="Potencial de Hidrogeno", blank=False)

    def __str__(self):
        return f"{self.paper_id}"


class CampaignPaperModel(models.Model):
    """
    ### Django Model
    Technical Data Model is a data set representation of variants papers and
    their campaign information.
    """

    class Meta:
        db_table_comment = "Papers de campañas"

    document_id = models.AutoField(primary_key=True)
    paper_reference = models.CharField(
        verbose_name="Referencia",
        choices=REFERENCES_CHOICES,
        max_length=50,
        blank=False,
    )
    paper_type = models.CharField(
        verbose_name="Tipo de ensayo",
        choices=PAPER_TYPES_CHOICES,
        max_length=20,
        blank=False,
    )
    year = models.DateField(verbose_name="Año", blank=False)
    location = models.CharField(
        verbose_name="Localidad",
        choices=LOCATIONS_CHOICES,
        default=DEFAULT_CHOICE_VALUE,
        max_length=50,
        blank=False,
    )
    latitude = models.IntegerField(verbose_name="Latitud", null=True)
    longitude = models.IntegerField(verbose_name="Longitud", null=True)

    paper_pepetition = models.IntegerField(
        verbose_name="Repeiciones del ensayo", default=1, blank=False
    )

    paper = models.ForeignKey(
        VarietyPaperModel,
        verbose_name="Ensayo",
        on_delete=models.CASCADE,
        to_field="paper_id",
    )

    def __str__(self):
        return f"{self.document_id}/{self.paper.paper_id}"
