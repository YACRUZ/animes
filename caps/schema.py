import graphene
from graphene_django import DjangoObjectType

from .models import Cap


class CapType(DjangoObjectType):
    class Meta:
        model = Cap


class Query(graphene.ObjectType):
    caps = graphene.List(CapType)

    def resolve_caps(self, info, **kwargs):
        return Cap.objects.all()