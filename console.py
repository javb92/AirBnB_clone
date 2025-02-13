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
import models
import sys
import inspect
import shlex


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
                models.storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(models.storage.all().keys()):
                    print(models.storage.all()[element])
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
            if HBNBCommand.verifyclass(arguments[0]):
                HBNBCommand.error_handler(4)
            else:
                HBNBCommand.error_handler(2)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                models.storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(models.storage.all().keys()):
                    del models.storage.all()[element]
                    models.storage.save()
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)

    def do_all(self, args):
        """ all method """
        tmp_list = []
        if len(args) is 0:
            stor_dict = models.storage.all()
            for obj_id in stor_dict.keys():
                obj = stor_dict[obj_id]
                tmp_list.append(str(obj))
            print(tmp_list)
        else:
            models.storage.reload()
            arguments = args.split()
            if HBNBCommand.verifyclass(arguments[0]):
                stor_dict = models.storage.all()
                for obj_id in stor_dict.keys():
                    if (arguments[0] in obj_id):
                        obj = stor_dict[obj_id]
                        tmp_list.append(str(obj))
                print(tmp_list)
            else:
                HBNBCommand.error_handler(2)

    def do_update(self, args):
        """ all method """
        arguments = shlex.split(args)
        if len(arguments) is 0:
            HBNBCommand.error_handler(1)
        elif len(arguments) is 1:
            if HBNBCommand.verifyclass(arguments[0]):
                HBNBCommand.error_handler(4)
            else:
                HBNBCommand.error_handler(2)
        else:
            if HBNBCommand.verifyclass(arguments[0]):
                models.storage.reload()
                element = arguments[0] + "." + arguments[1]
                if element in list(models.storage.all().keys()):
                    if len(arguments) is 2:
                        HBNBCommand.error_handler(5)
                    elif len(arguments) is 3:
                        HBNBCommand.error_handler(6)
                    else:
                        setattr(models.storage.all()[element],
                                arguments[2], arguments[3])
                        models.storage.all()[element].save()
                else:
                    HBNBCommand.error_handler(3)
            else:
                HBNBCommand.error_handler(2)

    def do_EOF(self, *args):
        """ EOF method """
        return (True)

    def do_quit(self, *args):
        """ Quit command to exit the program \n"""
        return (True)

    def emptyline(self):
        """
        empty line
        """
        pass

    def verifyclass(name_class):
        """
        verify class
        """
        my_classes = [
            "Review", "BaseModel", "City", "State", "User", "Amenity", "Place"
        ]
        if name_class in my_classes:
            return True
        else:
            return False

    def error_handler(num_error):
        """
        error handler
        """
        if num_error is 1:
            print("** class name missing **")
        elif num_error is 2:
            print("** class doesn't exist **")
        elif num_error is 3:
            print("** no instance found **")
        elif num_error is 4:
            print("** instance id missing **")
        elif num_error is 5:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def default(self, args):
        """
        default
        """
        argu = args.split(".")
        if len(argu) > 1:
            if argu[1] == "all()":
                self.do_all(argu[0])
            if argu[1] == "count()":
                sum = 0
                tmp_dic = models.storage.all()
                for key, value in tmp_dic.items():
                    if argu[0] in key:
                        sum += 1
                print(sum)
            if "show" in argu[1]:
                new_cut = argu[1].split('"')
                self.do_show(argu[0] + " " + new_cut[1])
            if "destroy" in argu[1]:
                new_cut = argu[1].split('"')
                self.do_destroy(argu[0] + " " + new_cut[1])

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
