from sqlalchemy import Column, BigInteger, String, sql
from utils.db_api.db_gino import TimeBasedModel


class User(TimeBasedModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    phone_number = Column(String(20))
    email = Column(String(100))
    city = Column(String(100))
    query: sql.Select
