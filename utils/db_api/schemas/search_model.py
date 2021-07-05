from sqlalchemy import Column, Integer, BigInteger, String, sql
from utils.db_api.db_gino import TimeBasedModel


class SearchModel(TimeBasedModel):
    __tablename__ = "search_models"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(100))
    destination = Column(String(100))
    time_period = Column(String(50))
    car_type = Column(String(100))
    weight_from = Column(Integer)
    weight_to = Column(Integer)
    volume_from = Column(Integer)
    volume_to = Column(Integer)
    telegram_id = Column(BigInteger)
    query: sql.Select

