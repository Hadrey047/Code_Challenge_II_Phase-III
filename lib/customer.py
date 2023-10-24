from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, desc, func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connect import Base
from customer


class Customer(Base):
    _tablename_ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)
    
    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant', creator=lambda res: Review(restaurant=res))
    
    def _repr_(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name} " \
            + f"{self.last_name}"
            
    def reviews(self):
        # should return a collection of all the reviews that the Customer has left
        return [reviews for reviews in session.query(Review).filter(Review.id == self.id)]
    
    def restaurants(self):
        # should return a collection of all the restaurants that the Customer has reviewed
        reviewed_ids = [restaurant_id[0] for restaurant_id in session.query(Review.restaurant_id).filter(Review.customer_id == self.id)]
        return [session.query(Restaurant).filter(Restaurant.id == restaurant_id).first() for restaurant_id in reviewed_ids]
    
    def full_name(self):
        # returns the full name of the customer, with the first name and the last name  concatenated, Western style.
        return f'{self.first_name} {self.last_name}'
    
    def favorite_restaurant(self):
        # returns the restaurant instance that has the highest star rating from this customer
        return [session.query(Restaurant).filter(Restaurant.id == restaurant_id[0]).first() for restaurant_id in session.query(Review.restaurant_id).filter(Review.customer_id == self.id).order_by(desc(Review.star_rating)).limit(1)]
    
    def add_review(self, restaurant, rating):
        # takes a restaurant (an instance of the Restaurant class) and a rating
        # creates a new review for the restaurant with the given restaurant_id
        review = Review(customer_id=self.id, restaurant_id=restaurant.id, rating=rating)
        session.add(review)
        session.commit()
    
    def delete_reviews(self, restaurant):
        # takes a restaurant (an instance of the Restaurant class) and
        # removes *all* their reviews for this restaurant
        # you will have to delete rows from the reviews table to get this to work!
        session.query(Review).filter_by(restaurant_id=restaurant.id, customer_id = self.id).delete()
        
