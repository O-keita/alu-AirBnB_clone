#!/usr/bin/python3
"""module documented"""
import cmd
import shlex
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """
        This will ne the command interpreter
    """

    valid_classes = ['BaseModel']

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
            Create a new instance of a module and
            it in the json file
        """

        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class doesn't exist **")
        elif commands[0] not in self.valid_classes:
            print("** class name missing **")
        else:
            new_class = BaseModel()
            new_class.save()
            print(new_class.id)
    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing *")
        elif len(commands) == 1:
            print("** instance id missing **")

        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")

        else:

            mydict = models.storage.all()
            key = "{}.{}".format(commands[0], commands[1])

            if key in mydict:
                print(mydict[key])

            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class
            name and id (save the change into the
            JSON file)
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            myobj = models.storage.all()
            key = "{}.{}".format(commands[0], commands[1])

            if key in myobj:
                del myobj[key]
            else:
                print("** no instance found **")


    def do_all(self, arg):
        """
            Prints all string representation
            of all instances based or not on the class name.
        """
        commands = shlex.split(arg)

        myobj = models.storage.all()

        if len(commands) == 0:
            for key, value in myobj.items():
                print(str(value))
                # print(key)

        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in myobj.items():

                if key.split(".")[0] == commands[0]:

                    print(str(value))
                
            

    def do_update(self, arg):
        """  Updates an instance based on the class
             name and id by adding or updating attribute
             (save the change into the JSON file)."""
    
        command = shlex.split(arg)
        myobj = models.storage.all()



        if len(command) == 0:
            print("** class name missing **")
        
        elif command[0] not in self.valid_classes:
            print("* class doesn't exist **")

        elif len(command) == 1:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(command[0], command[1])

            if key not in myobj:

                print("** no instance found **")

            elif len(command) == 2:
                print("** attribute name missing **")

            elif len(command) == 3:
                print("** value missing **")
            else:
                obj = myobj[key]
                attr_name = command[2]
                attr_value = command[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
        
if __name__ == "__main__":
    """documented"""
    HBNBCommand().cmdloop()
