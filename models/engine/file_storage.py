#!/usr/bin/python3
"""Module file_storage

This Module contains a definition for FileStorage Class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage Class

    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): A dictionary of instantiated objects.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dctn = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(dctn, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, encoding='utf8') as f:
                objects = json.load(f)
        except FileNotFoundError:
            FileStorage.__object = {}
