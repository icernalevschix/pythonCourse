import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from .models import Actor

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        db_using = "default"



class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    actors = graphene.List(ActorType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Actor.objects.get(pk=id)

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()

    
schema = graphene.Schema(query=Query)