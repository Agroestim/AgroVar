import graphene
import graphene_django

from api import models

# TODO: Definir los esquemas y mutaciones en base a los modelos y consultas
# relevantes que se realizaran en la aplicacion.


class VarietyPaperDataType(graphene_django.DjangoObjectType):
    """
    ### GraphQL-Django objectType
    Defines how `VarietyPaperModel` are represented in a GraphQL object type definition.
    """

    class Meta:
        model = models.VarietyPaperModel
        field = "__all__"


class TechnicalDataType(graphene_django.DjangoObjectType):
    """
    ### GrapQL-Django ObjectType
    Defines how `TechnicalDataModel` are represented in a GraphQL object type definition.
    """

    class Meta:
        model = models.TechnicalDataModel
        fields = "__all__"


class LocationRankingType(graphene_django.DjangoObjectType):
    class Meta:
        model = models.TechnicalDataModel
        fields = ("document_id", "year", "location")


class TechnicalDataQueryType(graphene.ObjectType):
    """
    ### Graphene ObjectType
    Represents a ranking
    """

    paper_variety_set = graphene.List(VarietyPaperDataType)
    """Represents a complete set of papers and varieties data."""

    location_ranking = graphene.List(LocationRankingType)

    def resolve_paper_variety_set(self, info):
        return models.VarietyPaperModel.objects.all()


SCHEMA = graphene.Schema(query=TechnicalDataQueryType)
