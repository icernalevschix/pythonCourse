import graphene
# import GraphQL_API.schema as schema
import graphoracle.schema as schema

class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)