#!/usr/bin/python3

"""Define FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file__path = 'file.json'
    __objects = {}

    def all(self):
        """Return all objects stored in the dictionnary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """Set in __objects the obj with the key <obj classname>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to JSON fie"""
        objects_copy = FileStorage.__objects.copy()
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }
        with open(FileStorage.__file__path, "w") as f:
            json.dump(objects_dict, f)

    
    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file__path, "r") as f:
                objects_dict = json.load(f)
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return

    def get_file_path():
        return (FileStorage.__file__path)
