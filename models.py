from sqlalchemy import Column, DateTime, String, Integer, func, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Proxy(Base):
    __tablename__ = "proxies"

    id = Column(String(50), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    proxy_address = Column(String(50))
    port = Column(String(10))
    valid = Column(Boolean())
    last_verification = Column(String(60))
    country_code = Column(String(2))
    city_name = Column(String(60))
    asn_name = Column(String(75))
    asn_number = Column(Integer())
    high_country_confidence = Column(Boolean)
    created_at = Column(String)

    def __repr__(self):
        return f"id: {self.id}, ip: {self.proxy_address}, 'port': {self.port}, 'country_code':{self.country_code}"
