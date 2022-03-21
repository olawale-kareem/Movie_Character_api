from .models import MovieCharacters
import graphene
from graphene_django import DjangoObjectType


class MovieCharactersType(DjangoObjectType):
    class Meta:
        model = MovieCharacters


class Query(graphene.ObjectType):
    characters = graphene.List(MovieCharactersType)

    def resolve_characters(self, info, **kwargs):
        return MovieCharacters.objects.all()
