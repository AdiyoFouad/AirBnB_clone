#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd, models, re
from models.base_model import BaseModel
from models.base_model import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    classes = {
        'BaseModel' : BaseModel()
        'User': User()
    }

    def default(self, line):
        """Commande innexistante"""
        print(f'Commande "{line}" doesn\'t exist')
        return

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """
        Usage: create <class name>
        Create a new instance of BaseModel
        """
        arg = line.split()
        
        if (len(arg) == 0):
            print("** class name is missing **")
        else:
            if (arg[0] not in HBNBCommand.classes.keys()):
                print("** class doesn't exist **")
            else:
                instance = HBNBCommand.classes[arg[0]]
                instance.save()
                print(instance.id)

    def do_show(self, line):
        """
        Usage: show <class name>  <id>
        Print the string representation of an instance based on the class name and id
        """

        args = line.split()
        if (len(args) == 0):
            print("** class name is missing **")
        elif (len(args) == 1):
            if (args[0] not in HBNBCommand.classes.keys()):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            key = args[0] + '.' + args[1]
            if (key not in all_objects.keys()):
                print("** no instance found **")
            else:
                print(str(all_objects[key]))

    def do_destroy(self, line):
        """
        Usage: destroy <class name>  <id>
        Delete an instance based on the class name and id
        """
        args = line.split()
        if (len(args) == 0):
            print("** class name is missing **")
        elif (len(args) == 1):
            if (args[0] not in HBNBCommand.classes.keys()):
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            key = args[0] + '.' + args[1]
            if (key not in all_objects.keys()):
                print("** no instance found **")
            else:
                del all_objects[key]

    def do_all(self, line):
        """
        Usage: all <optional <class name> >
        Print all string representation of all instances based or not on class
        """
        all_objects = []
        if (line == "" or line is None):
            for value in models.storage.all().values():
                all_objects.append(str(value))
            print(all_objects)
        else:
            if (line not in HBNBCommand.classes.keys()):
                print("** class doesn't exist **")
            else:
                for key, value in models.storage.all().items():
                    if (line in key):
                        all_objects.append(str(value))
            print(all_objects)

    def do_update(self, line):
        """
        Usage: update <class name> <id> <attribute name> <attribute value>
        Update an instance based on the class name and id by adding or update a attribute
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        all_objects = models.storage.all()

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        ins_id = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")
        elif classname not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif ins_id is None:
            print("** instance id missing **")
        else:
            key = classname + '.' + ins_id
            if key not in all_objects.keys():
                print("** no instance found **")
            else:
                if not attribute:
                    print("** attribute name missing **")
                elif attribute in ['id', 'created_at', 'updated_at']:
                    print(f"** attribute \"{attribute}\" can't be updated **")
                else:
                    if not value:
                        print("** value missing **")
                    else:
                        obj = all_objects[key]
                        if attribute in obj.__dict__.keys():
                            if not re.search('^".*"$', value):
                                try:
                                    if '.' in value:
                                        value = float(value)
                                    else:
                                        value = int(value)
                                except ValueError:
                                    print("** value missing **")
                                    return
                            else:
                                value = value.replace('"','')
                            if type(value) == type(obj.__dict__[attribute]):
                                obj.__dict__[attribute] = value
                                print("update")
                            else:
                                print("value error")
                        else:
                            if re.search('^".*"$', value):
                                value = value.replace('"','')
                                obj.__dict__[attribute] = value
                                print("update")
                            else:
                                print("** value missing **")                       
    
    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
