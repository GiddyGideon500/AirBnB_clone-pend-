#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

from datetime import datetime
import uuid


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        bs_dict = (
                {
                    k: (v.isoformat() if isinstance(v, datetime) else v)
                    for (k, v) in self.__dict__.items()
                }
        )
        bs_dict["__class__"] = self.__class__.__name__
        return bs_dict

    def __str__(self) -> str:
        """should print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
