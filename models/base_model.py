#!/usr/bin/python3
"""
the BaseModel class
"""
import models
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
        Base class for the other classes
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """
        initialize public instance attribute
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if "created_at" in kwargs:
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in kwargs:
            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        for key, val in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, val)

    def __str__(self):
        """
        return a string representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
        return string representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        save method
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        dictionary representation
        """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        if "_sa_instance_state" in cp_dct:
            del cp_dct["_sa_instance_state"]

        return (cp_dct)

    def delete(self):
        """
        calling the method delete
        """
        models.storage.delete(self)
