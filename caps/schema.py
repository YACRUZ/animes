import graphene
from graphene_django import DjangoObjectType
from .models import Cap
from graphql import GraphQLError
from django.db.models import Q
from users.schema import UserType
from caps.models import Cap, Vote


class CapType(DjangoObjectType):
    class Meta:
        model = Cap

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    caps = graphene.List(CapType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_caps(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulo__icontains=search) |
                Q(genero__icontains=search)
            )
            return Cap.objects.filter(filter)
        
        return Cap.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

#1
class CreateCap(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    temporada = graphene.String()
    genero = graphene.String()
    capitulos = graphene.Int()
    estudio = graphene.String()
    director = graphene.String()
    animacion = graphene.String()
    formato = graphene.String()
    adaptacion = graphene.String()
    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
        titulo = graphene.String()
        temporada = graphene.String()
        genero = graphene.String()
        capitulos = graphene.Int()
        estudio = graphene.String()
        director = graphene.String()
        animacion = graphene.String()
        formato = graphene.String()
        adaptacion = graphene.String()


    #3
    def mutate(self, info, titulo, temporada, genero, capitulos, estudio, director, animacion, formato, adaptacion):

        user = info.context.user or None

        cap = Cap(titulo=titulo, temporada=temporada, genero=genero, capitulos=capitulos, 
                   estudio=estudio, director=director, animacion=animacion, formato=formato, adaptacion=adaptacion,
                   posted_by=user,)
        cap.save()

        return CreateCap(
            id=cap.id,
            titulo=cap.titulo,
            temporada=cap.temporada,
            genero=cap.genero,
            capitulos=cap.capitulos,
            estudio=cap.estudio,
            director=cap.director,
            animacion=cap.animacion,
            formato=cap.formato,
            adaptacion=cap.adaptacion,
            posted_by=cap.posted_by
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    cap = graphene.Field(CapType)

    class Arguments:
        cap_id = graphene.Int()

    def mutate(self, info, cap_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        cap = Cap.objects.filter(id=cap_id).first()
        if not cap:
            raise GraphQLError('Invalid Cap!')

        Vote.objects.create(
            user=user,
            cap=cap,
        )

        return CreateVote(user=user, cap=cap)

#4
class Mutation(graphene.ObjectType):
    create_cap = CreateCap.Field()
    create_link = CreateCap.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)