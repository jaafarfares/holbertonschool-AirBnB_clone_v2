#!/usr/bin/python3
"""
Console Module
"""

import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def isfloat(x):
    """ lets check if x is a float"""

    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    """ check if x is int """
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    available_models = ["BaseModel",
                        "Amenity",
                        "City",
                        "Place",
                        "Review",
                        "State",
                        "User"]

    prompt = ("(hbnb) ")

    def do_quit(self, args):
        """ Method to exit the HBNB console"""
        exit()

    def do_EOF(self, args):
        """ Handles EOF to exit program """
        print()
        exit()

    def is_valid_arg(self, arg):
        """Checks if an argument is valid"""

        if "=" in arg:
            return True
        else:
            return False

    def do_create(self, args):
        """lets update the do_create function to allow for
        object creation with given parameters"""

        if not args:
            print("** class name missing **")
            return
        args = shlex.split(args)
        if args[0] not in self.available_models:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        for arg in args[1:]:
            if self.is_valid_arg(arg):
                key = arg.split('=')[0]
                val = arg.split('=')[1].replace('_', ' ')
                if isfloat(val):
                    val = float(val)
                elif isint(val):
                    val = int(val)
                setattr(new_instance, key, val)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """ Method to show an individual object """

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroys a specified object """

        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""

        storage.reload()
        try:
            if len(args) != 0:
                objects = storage.all(args)
            else:
                objects = storage.all()
        except NameError:
            print("** class doesn't exist **")
            return

        print(list(objects.values()))

    def emptyline(self):
        """ Overrides the emptyline method of CMD """

        pass

    def do_update(self, args):
        """ Updates a certain object with new info """

        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def do_count(self, args):

        obj_list = []
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if isinstance(val, eval(args)):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except BaseException:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
