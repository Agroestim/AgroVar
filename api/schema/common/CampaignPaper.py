import graphene
import graphene_django

from api import models


class CampaignPaperType(graphene_django.DjangoObjectType):
    """
    Graphene object type definition for Django `CampaignPaperModel`.
    """

    class Meta:
        description = ""
        model = models.CampaignPaperModel
        fields = "__all__"


class CampaignPaperQuery(graphene.ObjectType):
    """
    ### Varieties operation group

    Graphql endpoint for Varieties Operation Group.
    Represents the main query for all operations availables in Agrovar.

    - Location Ranking:
        Location ranking represents the result of comparing the
        campaigns by location and filtering the desired varieties.

    - Variety Comparator:
        Variety Comparator represents the result of filtering
        those varieties to be compared.
    """

    class Meta:
        description = "Representa la consulta principal para todas los grupos de operacioens disponibles en Agrovar."

    location_ranking = graphene.List(
        CampaignPaperType, locations=graphene.List(graphene.String)
    )

    variety_comparator = graphene.List(
        CampaignPaperType,
        varieties=graphene.List(graphene.String),
    )

    def resolve_location_ranking(self, info, locations: list[str]):
        related_ranking = models.CampaignPaperModel.objects.filter(
            location__in=[clean_location.upper() for clean_location in locations]
        )

        return related_ranking

    def resolve_variety_comparator(self, info, varieties: list[str]):
        related_varieties = models.CampaignPaperModel.objects.filter(
            paper__variety__in=[clean_variety.upper() for clean_variety in varieties]
        )

        return related_varieties
