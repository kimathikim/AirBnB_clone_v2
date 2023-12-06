#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {
    "User": User,
    "Place": Place,
    "City": City,
    "Review": Review,
    "Amenities": Amenity,
    "State": State,
}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for class dbStorage"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                objects = self.__session.query(clases[c]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()
