from django.db import models

# Create your models here.


class TechnicalDataFileModel(models.Model):
    file_id = models.AutoField(primary_key=True)
    gridfs_id = models.CharField(max_length=30, blank=True)
    file_name = models.CharField(max_length=40)


class VarietyPaperModel(models.Model):
    VARITIES_CHOICES = [
        ("BUCKSY200", "Buck SY 200"),
        ("LENOX", "Lenox"),
        ("ACA360", "ACA 360"),
        ("ACA365", "ACA 365"),
        ("ALGARROBBO", "Algarrobo"),
        ("ARSLAK", "Arslak"),
        ("BAGUETTE601", "Baguette 601"),
        ("BASILIO", "Basilio"),
        ("BG620", "Bg 620"),
        ("BG750", "Bg 750"),
        ("BIOINTA2004", "Biointa 2004"),
        ("BIOINTA3005", "Biointa 3005"),
        ("BIOINTA3006", "Biointa 3006"),
        ("CEDRO", "Cedro"),
        ("FLORIPAND", "Floripan 200"),
        ("GUAYABO", "Guayabo"),
        ("MSINTA119", "MS INTA 119"),
        ("ÑANDUBAY", "Ñandubay"),
        ("SURSEM2330", "Sursem 2330"),
    ]

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


class TechnicalDataModel(models.Model):
    """
    ### Django Model
    Technical Data Model is a data set representation of variants papers and
    their campaign information.
    """

    REFERENCES_CHOICES = [
        ("RED INTA 2022", "Red INTA 2022"),
        ("INTA LABOULAYE", "INTA Laboulaye"),
    ]
    PAPER_TYPES_CHOICES = [("VARIEDADES", "Variedades")]

    LOCATIONS_CHOICES = [
        ("ADELIA MARIA", "Adelia Maria"),
        ("BELL VILLE", "Bell Ville"),
        ("JUSTINIANO POSSE", "Justiniano Posse"),
        ("LA CARLOTA", "La Carlota"),
        ("LABOULAYE", "Laboulaye"),
        ("MARCOZ JUAREZ", "Marcos Juarez"),
        ("ONAGOITY", "Onagoity"),
    ]

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
        verbose_name="Localidad", choices=LOCATIONS_CHOICES, max_length=50
    )
    latitude = models.IntegerField(verbose_name="Latitud", null=True)
    longitude = models.IntegerField(verbose_name="Longitud", null=True)

    paper_pepetition = models.IntegerField(
        verbose_name="Repeiciones del ensayo", default=1, blank=False
    )

    paper_fk = models.ForeignKey(
        VarietyPaperModel,
        verbose_name="Ensayo",
        on_delete=models.CASCADE,
        to_field="paper_id",
    )

    def __str__(self):
        return f"{self.document_id}/{self.paper_fk.paper_id}"
