import graphene

import graphql_jwt
import caps.schema
import users.schema


class Query(users.schema.Query, caps.schema.Query, graphene.ObjectType):
    pass

class Mutations(users.schema.Mutation, caps.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)