import graphene

from api.schema.AgrovarMixedQueries import AgrovarMixedQueries

SCHEMA = graphene.Schema(query=AgrovarMixedQueries)
