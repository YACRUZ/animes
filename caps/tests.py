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
class LinkTestCase(GraphQLTestCase):
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