from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database import Base


class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    nitrogen = Column(Float)

    phosphorus = Column(Float)

    potassium = Column(Float)

    temperature = Column(Float)

    humidity = Column(Float)

    ph = Column(Float)

    rainfall = Column(Float)

    predicted_crop = Column(String)
