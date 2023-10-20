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


class TechnicalDataQueryType(graphene.ObjectType):
    """
    ### Graphene ObjectType
    Represents a ranking
    """

    location_ranking = graphene.List(TechnicalDataType, location=graphene.String())
    """Represents a list of varities ranked by location."""

    def resolve_location_ranking(self, info, location: str):
        location = location.upper()

        related_ranking = models.TechnicalDataModel.objects.filter(
            location__exact=location
        ).select_related("paper_fk")

        return related_ranking


SCHEMA = graphene.Schema(query=TechnicalDataQueryType)
