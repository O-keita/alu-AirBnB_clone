#!/usr/bin/python3
"""module documented"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
        This will ne the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == "__main__":
    """documented"""
    HBNBCommand().cmdloop()
