#!/usr/bin/python3
# File: console.py
# Author: Oluwatobiloba Light
"""
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import shlex
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"]

    def default(self, line):
        """
        Intercepts commands to test for class.syntax()
        """
        arguments = shlex.split(line)
        match = re.search()
        print(arguments)

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            arguments = line.split()
            if arguments[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                instance = eval("{}()".format(arguments[0]))
                print(instance.id)
                models.storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        obj = retreive_obj(models.storage.all(), line, self.__classes)
        print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        arguments = line.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            try:
                obj = data[key]
                data.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
         Prints all string representation of all instances based or not on the
         class name. Ex: $ all BaseModel or $ all
        """
        arguments = line.split()
        list = []
        if len(arguments) == 0:
            data = models.storage.all()
            for k, v in data.items():
                list.append("{}".format(v))
            print(list)
        else:
            if arguments[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                data = models.storage.all()
                for k, v in data.items():
                    if v.to_dict()['__class__'] == arguments[0]:
                        list.append("{}".format(v))
                print(list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute then saving the change into the JSON FILE.
        """
        arguments = shlex.split(line)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            data = models.storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if len(arguments) == 2:
                print("** attribute name missing **")
            elif len(arguments) == 3:
                try:
                    type(eval(arguments[2])) != dict
                except NameError:
                    print("** value missing **")
                return False
            else:
                try:
                    eval(arguments[3])
                except (SyntaxError, NameError):
                    arguments[3] = "'{}'".format(arguments[3])
                if arguments[2] not in ["id", "created_at", "updated_at"]:
                    try:
                        obj = data[key]
                        setattr(obj, arguments[2], eval(arguments[3]))
                        obj.save()
                    except KeyError:
                        print("** no instance found**")

    def do_EOF(self, line):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_count(self, line):
        match = re.search(r"\.", line)
        arg = [line[:match.span()[0]], line[match.span()[1]:]]
        if match is not None:
            command = [arg[1][:match.span()[0]], match.group()[1:-1]]
        print(command)


def retreive_obj(storage, line, __classes):
    """
    Retreives and returns an object from file storage
    """
    arguments = line.split()
    if len(arguments) == 0:
        return "** class name missing **"
    elif arguments[0] not in __classes:
        return "** class doesn't exist **"
    elif len(arguments) == 1:
        return "** instance id missing **"
    else:
        data = storage
        key = "{}.{}".format(arguments[0], arguments[1])
        try:
            return data[key]
        except KeyError:
            return "** no instance found **"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
