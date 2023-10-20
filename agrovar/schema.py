import graphene
import graphene_django

from api import models


class VarietyPaperDataType(graphene_django.DjangoObjectType):
    """
    ### Agrovar Internal
    Defines how `VarietyPaperModel` are represented in a GraphQL object type definition.
    """

    class Meta:
        model = models.VarietyPaperModel
        field = "__all__"


class TechnicalDataType(graphene_django.DjangoObjectType):
    """
    ### Agrovar Internal
    Defines how `TechnicalDataModel` are represented in a GraphQL object type definition.
    """

    class Meta:
        model = models.TechnicalDataModel
        fields = "__all__"


class LocationRankingType(graphene.ObjectType):
    """
    ### Agrovar GraphQL API
    This type represents a ranking sorted by location where each variants are compared with each other according to their location.
    """

    class Meta:
        description = "Consulta estatica para el ranking de variedades por localidad."


class VarietyComparatorType(graphene.ObjectType):
    """
    ### Agrovar Graphql API
    This type represents a list of varieties where each variant are compared with each other.
    """

    class Meta:
        description = "Consulta estatica para el comparador de variedades."

    year = graphene.Date()
    location = graphene.String()
    variety = graphene.String()


class TechnicalDataQueryType(graphene.ObjectType):
    """
    ### Agrovar Endpoint GraphQL API
    This type represents the endpoint of GraphQL for performing queries in general.

    """

    class Meta:
        description = "Representacion a la consulta de los analisis de las campañas y sus datos tecnicos."

    location_ranking = graphene.List(
        TechnicalDataType, location=graphene.String(required=True)
    )

    variety_comparator = graphene.List(
        # VarietyComparatorType, varieties=graphene.List(graphene.String)
        TechnicalDataType,
        varieties=graphene.List(graphene.String),
    )

    def resolve_location_ranking(self, info, location: str):
        related_ranking = models.TechnicalDataModel.objects.filter(
            location__exact=location.upper()
        ).select_related("paper_fk")

        return related_ranking

    def resolve_variety_comparator(self, info, varieties: list[str]):
        related_varieties = models.TechnicalDataModel.objects.select_related(
            "paper_fk"
        ).filter(
            variety__in=[map(lambda clean_variety: clean_variety.upper(), varieties)]
        )

        return related_varieties


SCHEMA = graphene.Schema(query=TechnicalDataQueryType)
