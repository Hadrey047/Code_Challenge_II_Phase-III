from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Database connection
engine = create_engine("sqlite:///models.db", echo=True)
Customer.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
