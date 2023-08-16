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
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    commands = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    # def default(self, line):
    #     """
    #     Intercepts commands to test for class.syntax()
    #     """
    #     methods = {
    #         "all": self.do_all,
    #         "show": self.do_show,
    #         "update": self.do_update,
    #         "destroy": self.do_destroy,
    #         "count": self.do_count
    #         }
    #     match = re.search(r"\.", line)
    #     if match is not None:
    #         classname = line[:match.span()[0]]
    #         method_name = line[match.span()[1]:]
    #         argument_list = re.search(r"\((.*?)\)", method_name)
    #         if argument_list is not None:
    #             method = re.search(r"\w*", method_name)
    #             if "all" in method.group():
    #                 call = "{}".format(classname)
    #                 methods[method.group()](call)
    #             elif "show" in method.group():
    #                 argument = argument_list.group()
    #                 id = re.search(r"\".*?\"", argument)
    #                 if id is not None and len(id.group()) > 2:
    #                     call = "{} {}".format(classname, eval(id.group()))
    #                     methods[method.group()](call)
    #                 else:
    #                     print("** instance id missing **")
    #             elif "update" in method.group():
    #                 arg = re.search(r'\(\s*"([^"]*)"\s*,\s*({.*})\s*\)',\
    # method_name)
    #                 id = arg.group(1)
    #                 dict_rep = arg.group(2)
    #                 print(id, dict_rep)
    #                 if id is not None and dict_rep is not None:
    #                     eval('"{}"'.format('**dict_rep'))
    #                     self.do_update(eval('{} "{}" "{}"'.format(classname,\
    # id, '**dict_rep')))
    #                     # methods[method.group()](eval("{} '{}' {}"\
    # .format(classname, id, '**dict_rep')))
    #                 # if len(arg.group()) == 0:
    #                 #     methods[method.group()](classname)
    #                 # elif len(arg.group()) == 1:
    #                 #     methods[method.group()]("{} {}".format(classname,\
    # arg[0]))
    #                 # elif len(arg.group()) == 2:
    #                 #     print(arg)
    #                 #     print(eval('{} {} "{}"'.format(classname,\
    # arg.group(0), '**arg.group(1)')))
    #                     # methods[method.group()](eval('{} "{}"'\
    # .format(classname, '**arg[0]')))
    #                 # else:
    #                 #     call = '{} {} {} "{}"'.format(classname,\
    # arg[0], arg[1], eval(arg[2]))
    #                 #     methods[method.group()](call)
    #             else:
    #                 print("*** Unknown syntax: {}".format(line))
    #         else:
    #             print("*** Unknown syntax: {}".format(line))

    #     else:
    #         print("*** Unknown syntax: {}".format(line))

    #     # if match is not None:
    #     #     argl = [line[:match.span()[0]], line[match.span()[1]:]]
    #     #     match = re.search(r"\((.*?)\)", argl[1])
    #     #     print("match is ", match)
    #     #     if match is not None:
    #     #         command = [argl[1][:match.span()[0]], match.group()[1:-1]]
    #     #         # print(command[1], argl[0])
    #     #         if command[0] in methods.keys():
    #     #             call = "{} {}".format(argl[0], command[1])
    #     #             print(argl[0], command[1])
    #     #             return methods[command[0]](call)

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        """
        _command = _classname = _id = _arguments = ''
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _classname = pline[:pline.find('.')]

            _command = pline[pline.find('.') + 1:pline.find('(')]
            if _command not in HBNBCommand.commands:
                raise Exception

            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                pline = pline.partition(', ')

                _id = pline[0].replace('\"', '')

                pline = pline[2].strip()
                if pline:
                    if pline[0] == "{" and pline[-1] == "}"\
                            and type(eval(pline)) is dict:
                        _arguments = pline
                    else:
                        _arguments = pline.replace(',', '')
            line = ' '.join([_command, _classname, _id, _arguments])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

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
            if arguments[0] not in self.classes:
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
        obj = retreive_obj(models.storage.all(), line, self.classes)
        print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        arguments = line.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
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
            if arguments[0] not in self.classes:
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
        classname = class_id = attr_name = attr_val = kwargs = ''

        args = line.partition(" ")
        if args[0]:
            classname = args[0]
        else:
            print("** class name missing **")
            return
        if classname not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            class_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = classname + "." + class_id

        if key not in models.storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                attr_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not attr_name and args[0] != ' ':
                attr_name = args[0]
            if args[2] and args[2][0] == '\"':
                attr_val = args[2][1:args[2].find('\"', 1)]

            if not attr_val and args[2]:
                attr_val = args[2].partition(' ')[0]

            args = [attr_name, attr_val]

        new_dict = models.storage.all()[key]

        for i, attr_name in enumerate(args):
            if (i % 2 == 0):
                attr_val = args[i + 1]
                if not attr_name:
                    print("** attribute name missing **")
                    return
                if not attr_val:
                    print("** value missing **")
                    return
                if attr_name in HBNBCommand.types:
                    attr_val = HBNBCommand.types[attr_name](attr_val)

                new_dict.__dict__.update({attr_name: attr_val})

        new_dict.save()

        # arguments = shlex.split(line)
        # if len(arguments) == 0:
        #     print("** class name missing **")
        # elif arguments[0] not in self.classes:
        #     print("** class doesn't exist **")
        # elif len(arguments) == 1:
        #     print("** instance id missing **")
        # else:
        #     data = models.storage.all()
        #     key = "{}.{}".format(arguments[0], arguments[1])
        #     if len(arguments) == 2:
        #         print("** attribute name missing **")
        #     elif len(arguments) == 3:
        #         try:
        #             type(eval(arguments[2]))
        #         except (NameError, SyntaxError):
        #             print("** value missing **")
        #     else:
        #         try:
        #             eval(arguments[3])
        #         except (SyntaxError, NameError):
        #             arguments[3] = "'{}'".format(arguments[3])
        #         if arguments[2] not in ["id", "created_at", "updated_at"]:
        #             try:
        #                 obj = data[key]
        #                 setattr(obj, arguments[2], eval(arguments[3]))
        #                 obj.save()
        #             except KeyError:
        #                 print("** no instance found**")

    def do_EOF(self, line):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_count(self, line):
        arguments = line.split()
        data = models.storage.all().values()
        count = 0
        for obj in data:
            if arguments[0] == obj.__class__.__name__:
                count += 1
        print(count)


def retreive_obj(storage, line, classes):
    """
    Retreives and returns an object from file storage
    """
    arguments = line.split()
    if len(arguments) == 0:
        return "** class name missing **"
    elif arguments[0] not in classes:
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
