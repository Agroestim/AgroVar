from django.contrib import admin

from api.models import TechnicalDataModel, VarietyPaperModel

# Register your models here.
admin.site.register(VarietyPaperModel)
admin.site.register(TechnicalDataModel)
