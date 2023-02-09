#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd, models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    classes = {
        'BaseModel' : BaseModel()
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
        Usage: create <class>
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
        Usage: show <class>  <id>
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
        Usage: destroy <class>  <id>
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
        Usage: all <optional <class> >
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
            

        
    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
