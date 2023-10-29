from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Database connection
engine = create_engine("sqlite:///db_setup.db", echo=True)

# Create the tables
Restaurant.Base.metadata.create_all(engine)
Customer.Base.metadata.create_all(engine)
Review.Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


