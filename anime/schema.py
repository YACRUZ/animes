import graphene

import caps.schema


class Query(caps.schema.Query, graphene.ObjectType):
    pass

class Mutations(caps.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)