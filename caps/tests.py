from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from caps.schema import schema
from caps.models import Cap

CAPS_QUERY = '''
 {
   caps {
     id
     titulo
     temporada
     genero
     capitulos
     estudio
     director 
     animacion
     formato
     adaptacion
   }
 }
'''
class CapTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.cap1 = mixer.blend(Cap)
        self.cap2 = mixer.blend(Cap)

    def test_caps_query(self):
        response = self.query(
            CAPS_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query caps results ")
        print (content)
        assert len(content['data']['caps']) == 2

    def test_createCap_mutation(self):

        response = self.query(
            CREATE_CAP_MUTATION,
            variables={'titulo': 'pochita', 'temporada': 'verano', 'genero': 'peleas', 'capitulos': 5, 'estudio': 'Trigger',
                       'director': 'miyazaki', 'animacion': '2d', 'formato': 'ova', 'adaptacion': 'original'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createCap": {'titulo': 'pochita', 'temporada': 'verano', 'genero': 'peleas', 'capitulos': 5, 'estudio': 'Trigger',
                       'director': 'miyazaki', 'animacion': '2d', 'formato': 'ova', 'adaptacion': 'original'}}, content['data']) 

CREATE_CAP_MUTATION = '''
 mutation createCapMutation($titulo: String, $temporada: String, $genero: String, $capitulos: Int, $estudio: String, $director: String, $animacion: String, $formato: String, $adaptacion: String) {
     createCap(titulo: $titulo, temporada: $temporada, genero: $genero, capitulos: $capitulos, estudio: $estudio, director: $director,
     animacion: $animacion, formato: $formato, adaptacion: $adaptacion) {
         titulo
         temporada
         genero
         capitulos
         estudio
         director 
         animacion
         formato
         adaptacion
     }
 }
'''

