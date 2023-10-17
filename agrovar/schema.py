import graphene
import graphene_django

from api import models

# TODO: Definir los esquemas y mutaciones en base a los modelos y consultas
# relevantes que se realizaran en la aplicacion.


class TechnicalDataType(graphene_django.DjangoObjectType):
    """
    ### GrapQL-Django ObjectType
    Defines how `TechnicalDataModel` are represented in a GraphQL object type definition.
    """

    class Meta:
        model = models.TechnicalDataModel
        fields = "__all__ "


class TechnicalDataQueryType(graphene.ObjectType):
    """
    ### Graphene ObjectType
    Represents a ranking
    """

    paper = graphene.Field(TechnicalDataType, required=True)

    def resolve_paper_by_campaing(self, info, campaign):
        get_related_papers_id = models.TechnicalDataModel.objects.filter(
            year__year=campaign
        ).get("paper")

        get_related_variety_paper = models.VarietyPaperModel.objects.filter(
            paper_id=get_related_papers_id
        ).get("variety")

    def resolve_paper_by_location(self, info, location):
        ...


# class ExcelFileType(graphene_django.DjangoObjectType):
#     """
#     ### GraphQL-Django ObjectType
#     Defines how `TechnicalDataFileModel` are represented in a GraphQL object type definition.
#     """

#     class Meta:
#         model = models.TechnicalDataFileModel
#         fields = ()


# class MutationExcelFile(graphene.Mutation):
#     class Arguments:
#         ...

#     mutable_field = graphene.Field(ExcelFileType)


# class QueryExcelFile(graphene.ObjectType):
#     excel_list = graphene.List(ExcelFileType)

#     def resolve_excel_list(self, info):
#         """"""
#         return models.TechnicalDataModel.objects.all()


schema = graphene.Schema(query=TechnicalDataQueryType)
