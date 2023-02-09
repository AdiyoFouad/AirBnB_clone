#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
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
        """Create a new instance of BaseModel"""
        arg = line.split()
        
        if (len(arg) == 0):
            print("class name is missing")
        else:
            if (arg[0] not in HBNBCommand.classes.keys()):
                print("class doesn't exist")
            else:
                instance = HBNBCommand.classes[arg[0]]
                instance.save()
                print(instance.id)

    

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
