#!/usr/bin/python3
""" Import cmd """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import sys
import inspect


class HBNBCommand(cmd.Cmd):
    """ This is the      console """
    prompt = "(hbnb) "

    def do_create(self, args):
        """ create method """

        if len(args) is 0:
            HBNBCommand.error_handler(1)
        else:
            arguments = args.split()
            if HBNBCommand.verifyclass(arguments[0]):
                new_object = eval(arguments[0])(arguments[1:])
                print(new_object.id)
                new_object.save()
            else:
                HBNBCommand.error_handler(2)

    def do_show(self, args):
        """ show method """
        arguments = args.split()
        if len(arguments) is 0:
            HBNBCommand.error_handler(1)
        elif len(arguments) is 1:
            HBNBCommand.error_handler(4)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(storage.all().keys()):
                    print(storage.all()[element])
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)

    def do_destroy(self, args):
        """ destroy method """
        arguments = args.split()
        if len(arguments) is 0:
            HBNBCommand.error_handler(1)
        elif len(arguments) is 1:
            HBNBCommand.error_handler(4)
        else:

            if HBNBCommand.verifyclass(arguments[0]):
                storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(storage.all().keys()):
                    del storage.all()[element]
                    storage.save()
                else:
                    HBNBCommand.error_handler(2)
            else:
                HBNBCommand.error_handler(2)

    def do_all(self, args):
        """ all method """
        if len(args) is 0:
            HBNBCommand.error_handler(1)
        else:
            storage.reload()
            arguments = args.split()

            if HBNBCommand.verifyclass(arguments[0]):

                storage_dict = storage.all()
                for key, values in storage_dict.items():

                    if arguments[0] == key.split(".")[0]:
                        print("______Dictionary ________")
                        print(storage.all())
                        print(storage_dict[key])
            else:
                HBNBCommand.error_handler(2)

    def do_update(self, args):
        """ all method """
        arguments = args.split()
        if len(arguments) is 0:
            HBNBCommand.error_handler(1)
        elif len(arguments) is 1:
            HBNBCommand.error_handler(4)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(storage.all().keys()):
                    if len(arguments) is 2:
                        HBNBCommand.error_handler(5)
                    elif len(arguments) is 3:
                        HBNBCommand.error_handler(6)
                    else:
                        provisional = storage.all()[element].to_dict()
                        provisional.update({arguments[2]: arguments[3]})
                        eval(arguments[0])(**provisional).save()
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)

    def do_EOF(self, *args):
        """ EOF method """
        print()
        return (True)

    def do_quit(self, *args):
        """ Quit command to exit the program \n"""
        return (True)

    def emptyline(self):
        pass

    def verifyclass(name_class):
        my_classes = [
            "Review", "BaseModel", "City", "State", "User", "Amenity", "Place"
        ]
        if name_class in my_classes:
            return True
        else:
            return False

    def error_handler(num_error):
        if num_error is 1:
            print("** class name missing **")
        elif num_error is 2:
            print("** class doesn't exist **'")
        elif num_error is 3:
            print("** no instance found **")
        elif num_error is 4:
            print("** instance id missing **")
        elif num_error is 5:
            print("** attribute name missing **")
        else:
            print("** value missing **")

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
