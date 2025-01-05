#!/usr/bin/python3
"""
Database storage engine model
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

user = os.getenv('HBNB_MYSQL_USER', "default_usr")
psswd = os.getenv('HBNB_MYSQL_PWD', "default_pwd")
host = os.getenv('HBNB_MYSQL_HOST', "localhost")
db = os.getenv('HBNB_MYSQL_DB', "default_db")


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes that database attributes"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, psswd, host, db), pool_pre_ping=True)

        # Drop all tables if env var HBNB_ENV is 'test'
        if os.getenv('HBNB_ENV', 'default_env') == 'test':
            Base.metadata.drop_all(self.__engine)
            # self.drop_all_tables()

    def all(self, cls=None):
        """Return all objects depending on the class"""
        obj_dict = {}
        if cls is None:
            query_res = []
            for model_class in [User, State, City, Amenity, Place, Review]:
                query_res.extend(self.__session.query(model_class).all())
        else:
            query_res = self.__session.query(cls).all()

        obj_dict = {
                f'{type(obj).__name__}.{obj.id}': obj
                for obj in query_res
                }

        return obj_dict

    def new(self, obj):
        """Adds the object to current database session"""
        if obj:
            self.__session.add(obj)
        else:
            return

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj and hasattr(obj, '_sa_instance_state'):
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """Loads the database into active session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
