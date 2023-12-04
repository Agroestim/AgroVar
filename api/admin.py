from django.contrib import admin

from api.models import CampaignPaperModel, VarietyPaperModel

# Register your models here.
admin.site.register(VarietyPaperModel)
admin.site.register(CampaignPaperModel)
