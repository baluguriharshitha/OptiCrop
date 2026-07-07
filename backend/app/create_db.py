from app.database import Base, engine

from app.models.user import User
from app.models.crop import Crop
from app.models.prediction import Prediction

Base.metadata.create_all(bind=engine)

print("Database Created Successfully!")
