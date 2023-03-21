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
        cap = Cap(titulo=titulo, temporada=temporada, genero=genero, capitulos=capitulos, 
                   estudio=estudio, director=director, animacion=animacion, formato=formato, adaptacion=adaptacion)
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
            adaptacion=cap.adaptacion
        )


#4
class Mutation(graphene.ObjectType):
    create_cap = CreateCap.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)