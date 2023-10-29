from requests import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from models.Customer import Customer
from models.Review import Review  # Import Customer

Base = declarative_base()

class Restaurant(Base):
  __tablename__ = 'restaurants'

  id = Column(Integer(), primary_key=True)
  name = Column(String())
  price = Column(Integer())

  reviews = relationship('Review', back_populates='restaurant')
  users = association_proxy('reviews', 'customer', creator=lambda cust: Review(customer=cust))

  def customers(self):
    reviewer_ids = [review.customer_id for review in self.reviews]
    return [session.query(Customer).filter(Customer.id == customer_id).first() for customer_id in reviewer_ids]
