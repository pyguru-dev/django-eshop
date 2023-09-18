import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class AuthenticationMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    login = mutations.ObtainJSONWebToken.Field()
    # verify_account = mutations.VerifyAccount.Field()
    update_account = mutations.UpdateAccount.Field()