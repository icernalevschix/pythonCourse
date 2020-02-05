from django.db import models
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
from .database import etl_base

from datetime import datetime
import graphene

class Clients(etl_base):
    __tablename__   = 'EAGLE_CLIENTS'
    __table_args__  = {'schema': 'INF_MONITOR'}
    instance        = Column(Integer, primary_key=True)
    name            = Column(String)
    code            = Column(String)
    start_date      = Column(DateTime)
    finish_date     = Column(DateTime)
    type            = Column(String)
    regions_allowed = Column(Integer)
    timezone        = Column(String)

class DisClients(etl_base):
    __tablename__   = 'CLIENT'
    __table_args__  = {'schema': 'MSGCENTER_DBO'}
    client_seqno    = Column(Integer, primary_key=True)
    client_id       = Column(String)
    client_name     = Column(String)
    client_status   = Column(String)
    update_date     = Column(DateTime,default=func.now())
    update_source   = Column(String)


class Databases(etl_base):
    __tablename__   = 'DATABASES'
    __table_args__  = {'schema':'INF_MONITOR'}
    instance        = Column(Integer,primary_key=True)
    sid             = Column(String)
    client          = Column(Integer,ForeignKey('INF_MONITOR.EAGLE_CLIENTS.instance'))
    dataguard       = Column(String)
    status          = Column(String)
    tnsname         = Column(String)
    environment     = Column(String)
    oracle_version  = Column(String)
    pace_version    = Column(String)
    star_version    = Column(String)
    vip             = Column(String)
    creation_date   = Column(DateTime)
    all_clients     = relationship(
        Clients,
        backref=backref(
            'all_databases',
            uselist = True,
            cascade = 'delete,all'
        )
    )


class VendorProduct(etl_base):
    __tablename__           = 'VENDOR_PRODUCT'
    __table_args__          = { 'schema' : 'DIS_HUB' }
    vendor_product_seqno    = Column(Integer, primary_key=True)
    vendor_seqno            = Column(Integer, ForeignKey('DIS_HUB.VENDOR.vendor_seqno'))
    product_name            = Column(String)
    product_description     = Column(String)
    contact_person          = Column(String)
    contact_info            = Column(String)
    update_date             = Column(DateTime,default=func.now())
    update_source           = Column(String)


class Vendor(etl_base):
    __tablename__   = 'VENDOR'
    __table_args__  = {'schema': 'DIS_HUB'}
    vendor_seqno    = Column(Integer, primary_key=True)
    vendor_id       = Column(String)
    vendor_name     = Column(String)
    vendor_desc     = Column(String)
    update_date     = Column(DateTime,default=func.now())
    update_source   = Column(String)
    vendor_type     = Column(String)
    website         = Column(String)
    portal          = Column(String)
    portal_user     = Column(String)
    portal_pwd      = Column(String)
    vendor_info     = Column(String)
    all_vendor_products = relationship(VendorProduct, 
        backref= backref('all_vendors', uselist = True, cascade = 'delete,all'))


class Interface(etl_base):
    __tablename__   = 'INTERFACE'
    __table_args__  = {'schema': 'DIS_HUB'}
    intrf_seqno     = Column(Integer, primary_key=True) 
    intrf_id        = Column(String)
    intrf_name      = Column(String)
    intrf_desc      = Column(String)
    intrf_status    = Column(String)
    update_date     = Column(DateTime,default=func.now())
    update_source   = Column(String)
    model           = Column(String)
    eagleml_version = Column(String) 
    eagle_version   = Column(String)
    support_ejm     = Column(String)
    tsd_location    = Column(String)
    interface_ba    = Column(String)
    interface_dev   = Column(String)
    vendor_seqno    = Column(Integer, ForeignKey('DIS_HUB.VENDOR.vendor_seqno'))
    all_vendors     = relationship(
        Vendor,
        backref=backref('all_interfaces',
                        uselist = True,
                        cascade = 'delete,all')) 


class Subscription(etl_base):
    __tablename__   = 'SUBSCRIPTION'
    __table_args__  = {'schema': 'DIS_HUB'}
    subscr_seqno    = Column(Integer, primary_key=True)
    intrf_seqno     = Column(Integer,ForeignKey('DIS_HUB.INTERFACE.intrf_seqno'))
    client_seqno    = Column(Integer,ForeignKey('INF_MONITOR.DATABASES.instance'))
    subscr_notes    = Column(String)
    active_flag     = Column(String)
    update_date     = Column(DateTime, default=func.now())
    update_source   = Column(String)
    all_databases   = relationship(
        Databases,
        backref=backref(
            'all_subscriptions',
            uselist = True,
            cascade = 'delete,all'
        )
    )
    all_interfaces = relationship(
        Interface,
        backref=backref(
            'all_subscriptions',
            uselist = True,
            cascade = 'delete,all'
        )
    )

class ParamsEnum(etl_base):
    __tablename__        = 'PARAMS_ENUM'
    __table_args__       = {'schema': 'DIS_HUB'}    
    params_enum_seqno    = Column(Integer, primary_key = true)
    parameter_code       = Column(String)
    parameter_desc       = Column(String)
    parameter_data_type  = Column(String)
    update_date          = Column(DateTime, default = func.now())
    update_source        = Column(String)
    parameter_owner      = Column(String)

class InterfaceParams(etl_base):
    __tablename__        = 'INTERFACE_PARAM'
    __table_args__       = {'schema': 'DIS_HUB'}
    intrf_param_seqno    = Column(Integer, primary_key=True)
    environment          = Column(String, primary_key=True)
    intrf_seqno          = Column(Integer, ForeignKey('DIS_HUB.INTERFACE.intrf_seqno'))
    parameter_code       = Column(String, ForeignKey('DIS_HUB.PARAMS_ENUM.parameter_code'))
    parameter_value      = Column(String)
    parameter_blob_value = Column(String)
    update_date          = Column(DateTime, default=func.now())
    update_source        = Column(String)
    all_interfaces       = relationship(Interface,
        backref=backref('all_interface_parameters',
        uselist = True ))
    all_params_enum      = relationship(ParamsEnum,
        backref=backref('all_interface_parameters',
        uselist = True ))


class ClientParams(etl_base):
    __tablename__       = 'CLIENT_PARAM'
    __table_args__      = {'schema':'DIS_HUB'}
    client_param_seqno  = Column(Integer, primary_key=True)
    client_seqno        = Column(Integer, ForeignKey('INF_MONITOR.DATABASES.instance'))
    parameter_code      = Column(String, ForeignKey('DIS_HUB.PARAMS_ENUM.parameter_code'))
    parameter_value     = Column(String)
    update_date         = Column(DateTime, default=func.now())
    update_source       = Column(String)
    all_databases       = relationship(Databases, 
        backref=backref('all_client_parameters', 
        uselist = True ))
    all_params_enum      = relationship(ParamsEnum,
        backref=backref('all_client_parameters',
        uselist = True ))


class SubscriptionParams(etl_base):
    __tablename__               = 'SUBSCRIPTION_PARAM'
    __table_args__              = {'schema':'DIS_HUB'}
    subscr_param_seqno          = Column(Integer, primary_key=True)
    subscr_seqno                = Column(Integer, ForeignKey('DIS_HUB.SUBSCRIPTION.subscr_seqno'))
    subscription_param_code     = Column(String, ForeignKey('DIS_HUB.PARAMS_ENUM.parameter_code'))
    subscription_param_value    = Column(String)
    update_date                 = Column(DateTime, default=func.now())
    update_source               = Column(String)
    all_subscriptions           = relationship(Subscription,
        backref=backref('all_subscription_parameters',
        uselist = True))
    all_params_enum      = relationship(ParamsEnum,
        backref=backref('all_subscription_parameters',
        uselist = True ))


class SubscriptionList(graphene.ObjectType):
    subscr_seqno = graphene.Int()
    intrf_seqno = graphene.Int()
    intrf_id = graphene.String()
    client_seqno = graphene.Int()
    tnsname = graphene.String()
    code = graphene.String()
    subscr_notes = graphene.String()
    active_flag = graphene.String()
    update_date = graphene.String()
    update_source = graphene.String()


class FeedTypes(etl_base):
    __tablename__        = 'FEED_TYPES'
    __table_args__       = {'schema': 'DIS_HUB'}    
    feed_type            = Column(String, primary_key = true)
    long_desc            = Column(String)
    short_desc           = Column(String)
    upd_datetime         = Column(DateTime, default = func.now())
    upd_user             = Column(String)




class PortalUsers(etl_base):
    __tablename__       = 'PORTAL_USERS'
    __table_args__      = {'schema':'DIS_HUB'}
    userSeqNo          = Column('user_seqno',Integer, primary_key=True)
    userName            = Column('username',String)
    password            = Column(String)
    email               = Column(String)
    role                = Column(String)
    update_date         = Column(DateTime, default=func.now())


class UserDetails(graphene.ObjectType):
    userSeqNo      = graphene.Int()
    userName        = graphene.String()
    password        = graphene.String()
    email           = graphene.String()
    role            = graphene.String()
    access_token    = graphene.String()
    refresh_token   = graphene.String()
    message         = graphene.String()
    update_date     = graphene.DateTime()
