import graphene
from graphene import ObjectType
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery, ObjectType):
    pass