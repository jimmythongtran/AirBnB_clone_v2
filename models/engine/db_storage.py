#!/usr/bin/python3
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db))

        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        queries = [User, State, City, Amenity, Place, Review]
        queriesDict = {}
        if cls is None:
            for i in queries:
                for info in self.__session.query(i):
                    queriesDict[data.__dict__["id"]] = info
        else:
            for info in self.__session(cls):
                queriesDict[data.__dict__["id"]] = info
        return queriesDict

    def new(self, obj):
        if !obj:
            self.__session(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if !obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.remove(self.__session)
