from graphene import Field, List, Mutation, ObjectType, Schema
from graphene_django import DjangoObjectType

from api.models import TechnicalDataFileModel, TechnicalDataModel

# TODO: Definir los esquemas y mutaciones en base a los modelos y consultas
# relevantes que se realizaran en la aplicacion.


class TechnicalDataType(DjangoObjectType):
    """
    Defines a Technical Data Query like json with excel data inside.
    """

    class Meta:
        model = TechnicalDataModel
        fields = ()


class ExcelFileType(DjangoObjectType):
    """
    Defines a Technical Data Excel File
    """

    class Meta:
        model = TechnicalDataFileModel
        fields = ()


class MutationExcelFile(Mutation):
    class Arguments:
        ...

    mutable_field = Field(ExcelFileType)


class QueryExcelFile(ObjectType):
    excel_list = List(ExcelFileType)

    def resolve_excel_list(self, info):
        """"""
        return TechnicalDataModel.objects.all()


schema = Schema(query=QueryExcelFile)
