#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


metadata = Base.metadata

"""This is the association table between place and amenity """
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(69),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    gbl_storage = environ.get('HBNB_TYPE_STORAGE')
    if gbl_storage == 'db':
        reviews = relationship('Review',
                               backref='places', cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='places',
                                 cascade='all, delete')
    else:
        @property
        def reviews(self):
            """Return all reviews related for a state"""
            all_reviews = models.storage.all("Review")
            own_reviews = []
            for value in all_reviews.values():
                if self.id == value.place_id:
                    own_reviews.append(value)
            return own_reviews

        @property
        def amenities(self):
            """ Returns the list of Amenity instances """
            all_amenities = models.storage.all('Amenity')
            own_amenity = []
            for key in all_amenities.keys():
                key_split = key.split(".")
                if key_split[1] in self.amenity_ids:
                    own_amenity.append(all_amenities[key])
            return own_amenity

        @amenities.setter
        def amenities(self, obj=None):
            """ Append amenity's id to amenity_ids"""
            obj_class = type(obj).__name__
            if obj is None or obj_class != 'Amenity':
                return
            self.amenity_ids.append(obj.id)
