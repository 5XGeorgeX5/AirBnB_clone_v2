#!/usr/bin/python3
"""Create a new engine"""
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the database session

        Args:
            cls (class, optional): class to be queried. Defaults to None.

        Returns:
            dict: the queried class
        """
        if cls is None:
            classes = [City, User, Place, Review, Amenity]
            objs = self.__session.query(State).all()
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add obj to the database

        Args:
            obj (object): object to be added
        """
        self.__session.add(obj)

    def save(self):
        """Commit the changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database

        Args:
            obj (object, optional): object to be deleted. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        start_session = scoped_session(session_factory)
        self.__session = start_session()

    def close(self):
        """call remove() method"""
        self.__session.close()
