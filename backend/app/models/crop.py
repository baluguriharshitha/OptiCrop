from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database import Base


class Crop(Base):

    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)

    crop_name = Column(String, unique=True)

    optimal_ph = Column(Float)

    optimal_temperature = Column(Float)

    water_requirement = Column(String)

    description = Column(String)
