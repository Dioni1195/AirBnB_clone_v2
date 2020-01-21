#!/usr/bin/python3
""" This is the engine to the DB storage"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from os import environ
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session

class DBStorage:
    """ Class to manage the storage in th DataBase
        Args:
        __engine(str): The engine
        __session(str): The session
    """
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        hst = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(user, pwd, hst, db), pool_pre_ping=True)
        #Base.metadata.create_all(self.__engine)
        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()
        hbnb_env = environ.get('HBNB_ENV')
        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Prints all the objects """

        classes = [State, City, User, Place, Review, Amenity]
        dict_return = {}

        if cls is None:
            for table_name in classes:
                for table in self.__session.query(table_name).all():
                    dict_return["{}.{}".format(table_name.__name__, table.id)] = table
        else:
            for table in self.__session.query(cls).all():
                dict_return["{}.{}".format(cls.__class__, table.id)] = table.to_dict()

        return dict_return

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """  commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        Session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_maker)
        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.remove()
