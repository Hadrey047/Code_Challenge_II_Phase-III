from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.Customer import Customer  # Import Customer
from models.Restaurant import Restaurant  # Import Restaurant

Base = declarative_base()

class Review(Base):
  __tablename__ = 'reviews'

  id = Column(Integer(), primary_key=True)
  star_rating = Column(Integer())
  restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
  customer_id = Column(Integer(), ForeignKey('customers.id'))

  customer = relationship('Customer', back_populates='reviews')
  restaurant = relationship('Restaurant', back_populates='reviews')
