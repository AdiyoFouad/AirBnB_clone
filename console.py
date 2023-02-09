#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

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
        var = line.split()
        print(var)



    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
