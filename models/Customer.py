from requests import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from models.Restaurant import Restaurant
from models.Review import Review  # Import Review

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)

    reviews = relationship('Review', back_populates='customer')  # Use 'Review' class
    restaurants = association_proxy('reviews', 'restaurant', creator=lambda res: Review(restaurant=res))

    def restaurants(self):
        reviewed_ids = [review.restaurant_id for review in self.reviews]
        return [session.query(Restaurant).filter(Restaurant.id == restaurant_id).first() for restaurant_id in reviewed_ids]

