from .database import etl_engine, etl_db_session
from .models import FeedTypes as FeedTypesModel
import graphene
from datetime import datetime
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene_django.types import DjangoObjectType, ObjectType


class FeedTypes( SQLAlchemyObjectType ):
    class Meta:
        model = FeedTypesModel
        interfaces = (relay.Node, )


class Query(ObjectType):

    all_feed_types = SQLAlchemyConnectionField(FeedTypes._meta.connection,sort = None)

    
schema = graphene.Schema(query=Query, types = [FeedTypes,])