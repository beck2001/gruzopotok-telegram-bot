from sqlalchemy import Column, Integer, BigInteger, String, sql
from utils.db_api.db_gino import TimeBasedModel


class Cargo(TimeBasedModel):
    __tablename__ = "cargos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    source = Column(String(100))
    destination = Column(String(100))
    time_period = Column(String(50))
    distance = Column(Integer)
    car_type = Column(String(100))
    weight_from = Column(Integer)
    weight_to = Column(Integer)
    volume_from = Column(Integer)
    volume_to = Column(Integer)
    client_name = Column(String(100))
    client_phone_number = Column(String(20))
    client_email = Column(String(100))
    telegram_id = Column(BigInteger)
    query: sql.Select

