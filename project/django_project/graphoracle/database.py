from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.orm import scoped_session, sessionmaker

import cx_Oracle


ip = '10.70.173.153'
port = 42511
SID = 'etld003'
dns_tns = cx_Oracle.makedsn(ip, port, SID)

oracle_connect = cx_Oracle.connect('MCINSTALL','Eagle_2015',dns_tns)


etl_engine = create_engine("oracle+cx_oracle://dis_hub:dis_test_hub1@10.70.147.92:42511/inftst6")
etl_db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=etl_engine))

etl_base = declarative_base()
etl_base.query = etl_db_session.query_property()
