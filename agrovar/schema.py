from graphene import List, ObjectType, Schema
from graphene_django import DjangoObjectType

from api.models import TecDataExcelFile


class ExcelFileType(DjangoObjectType):
    class Meta:
        model = TecDataExcelFile
        fields = ("file_id", "file_name")


class QueryExcelFile(ObjectType):
    excel_list = List(ExcelFileType)

    def resolve_excel_list(self, info):
        """"""
        return TecDataExcelFile.objects.first().file_name


schema = Schema(query=QueryExcelFile)
