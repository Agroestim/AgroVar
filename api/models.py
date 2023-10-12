from django.db import models

# Create your models here.


class TechnicalDataFileModel(models.Model):
    file_id = models.AutoField(primary_key=True)
    gridfs_id = models.CharField(max_length=30, blank=True)
    file_name = models.CharField(max_length=40)


class VarietyPaperModel(models.Model):
    VARITIES_CHOICES = [
        ("", "Buck SY 200"),
        ("", "Lenox"),
        ("", "ACA 360"),
        ("", "Algarrobo"),
        ("", "Arslak"),
        ("", "Baguette 601"),
        ("", "Basilio"),
        ("", "Bg 620"),
        ("", "Bg 750"),
        ("", "Biointa 2004"),
        ("", "Biointa 3005"),
        ("", "Biointa 3006"),
        ("", "Cedro"),
        ("", "Floripan 200"),
        ("", "Guayabo"),
        ("", "MS INTA 119"),
        ("", "Ñandubay"),
        ("", "Sursem 2330"),
    ]

    paper_id = models.BigAutoField(primary_key=True)
    variety = models.CharField(
        name="Variedad", choices=VARITIES_CHOICES, max_length=50, blank=False
    )
    humidity_percentage = models.FloatField(name="Humedad (%)", blank=False)
    performance = models.IntegerField(name="Redimiento (kg/ha)", blank=False)
    relative_performance = models.IntegerField(name="Redimiento Relativo", blank=False)
    grains_count = models.IntegerField(name="Numero de granos", blank=False)
    grains_per_spike = models.IntegerField(name="Granos por espiga", blank=False)
    weight_per_thousand_grains = models.FloatField(
        name="Peso por mil granos", blank=False
    )
    proteins_percentage = models.FloatField(name="Proteinas (%)", blank=False)
    ph = models.FloatField(name="Potencial de Hidrogeno", blank=False)


class TechnicalDataModel(models.Model):
    REFERENCES_CHOICES = [("", "Red INTA 2022"), ("", "INTA Laboulaye")]
    PAPER_TYPES_CHOICES = [("", "Variedades")]

    LOCATIONS_CHOICES = [
        ("", "Adelia Maria"),
        ("", "Bell Ville"),
        ("", "Justiniano Posse"),
        ("", "La Carlota"),
        ("", "Laboulaye"),
        ("", "Marcos Juarez"),
        ("", "Onagoity"),
    ]

    document_id = models.AutoField(primary_key=True)
    paper_reference = models.CharField(
        name="Referencia", choices=REFERENCES_CHOICES, max_length=50, blank=False
    )
    paper_type = models.CharField(
        name="Tipo de ensayo", choices=PAPER_TYPES_CHOICES, max_length=20, blank=False
    )
    year = models.DateField(name="Año", blank=False)
    location = models.CharField(
        name="Localidad", choices=LOCATIONS_CHOICES, max_length=50
    )
    latitude = models.IntegerField(name="Latitud", blank=True)
    longitude = models.IntegerField(name="Longitud", blank=False)

    paper_pepetition = models.IntegerField(
        name="Repeiciones del ensayo", default=1, blank=False
    )
