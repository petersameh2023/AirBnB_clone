#!/usr/bin/python3
""" Console Class for AirBnB Clone"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

my_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class for HBNB"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, line):
        """
        Coustmize command line and it's arguments
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <dictionary representation>)
        """
        if '.' not in line:
            print("** class name missing **")
            return
        parts = line.split('.')
        if len(parts) > 2:
            cls_name = parts[0]
            command = ".".join(parts[i] for i in range(1, len(parts)))
        if len(parts) == 2:
            cls_name, command = parts

        if command == "all()" and cls_name in my_classes:
            self.do_all(cls_name)
        elif command == "count()" and cls_name in my_classes:
            self.do_count(cls_name)
        elif 'show(' == command[:5] and cls_name in my_classes\
                and command[-1] == ')':
            id = command[6:-2]
            self.do_show(cls_name + " " + id)
        elif 'destroy(' == command[:8] and cls_name in my_classes\
                and command[-1] == ')':
            id = command[9:-2]
            self.do_destroy(cls_name + " " + id)
        elif 'update(' == command[:7] and cls_name in my_classes\
                and command[-1] == ')':
            print
            if command[7:-1] == '':
                print("** instance id missing **")
                return
            # Handle Errors
            my_args = command[7:-1].split(',')
            if len(my_args) == 2 and '{' not in command:
                print("** value missing **")
                return
            if len(my_args) == 1 and '{' not in command:
                print("** attribute name missing **")
                return
            # Handle Dict
            if '{' in command and '}' in command:
                dict_split = command[7:-1].split(" {")
                if len(dict_split) == 2:
                    id = dict_split[0].strip('",')
                    my_dict = "{" + dict_split[1]
                    my_dict = eval(my_dict)
                    for key, value in my_dict.items():
                        final_line = cls_name + ' ' + id + ' ' +\
                                key + ' ' + str(value)
                        self.do_update(final_line)
                    return
            #  4 values class-id-key- LIST
            if len(my_args) > 3:
                id, key = my_args[0], my_args[1]
                value = ",".join(my_args[i] for i in range(2, len(my_args)))
                id = id.strip('"')
                key = key.strip(' "')
                value = value.strip(' ')
                final_line = cls_name + " " + id + " " + key + " " + value
                self.do_update(final_line)
                return
            # Handle 4 values class-id-key-value
            elif len(my_args) == 3:
                id, key, value = my_args
                id = id.strip('"')
                key = key.strip(' "')
                value = value.strip(' ')
                final_line = cls_name + " " + id + " " + key + " " + value
                self.do_update(final_line)
                return

        else:
            if not parts[0]:
                print("** class name missing **")
            elif parts[0] not in my_classes:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program when you press ctrl + c"""
        print("")
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        If the class name is missing,
        print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ create MyModel)
        """
        if not line:
            print("** class name missing **")
        elif line not in my_classes:
            print("** class doesn't exist **")
        else:
            myobj = my_classes[line]()
            myobj.save()
            print(myobj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing **
        If the class name doesn’t exist, print ** class doesn't exist **
        If the id is missing, print ** instance id missing **
        If the instance of the class name doesn’t exist for the id,
        print ** no instance found **
        """
        my_args = line.split()

        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in my_classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            for object in obj_dict.values():
                Say_my_name = object.__class__.__name__
                if object.id == my_args[1] and Say_my_name == my_args[0]:
                    print(object)
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing **
        If the class name doesn’t exist, print ** class doesn't exist **
        If the id is missing, print ** instance id missing **
        If the instance of the class name doesn’t exist for the id
        print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        my_args = line.split()
        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in my_classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            for object_key in obj_dict.keys():
                if object_key == "{}.{}".format(my_args[0], my_args[1]):
                    del obj_dict[object_key]
                    models.storage.save()
                    break
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ all MyModel)
        """
        my_args = line.split()
        if len(my_args) == 0:
            Mylist = []
            dict_obj = models.storage.all()
            for obj in dict_obj.values():
                Mylist.append(str(obj))
            print(Mylist)
        elif len(my_args) > 0 and my_args[0] not in my_classes:
            print("** class doesn't exist **")
        elif len(my_args) == 1:
            Mylist = []
            dict_obj = models.storage.all()
            for obj in dict_obj.values():
                if obj.__class__.__name__ == my_args[0]:
                    Mylist.append(str(obj))
            print(Mylist)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        my_args = line.split()
        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in my_classes:
            print(my_args[0])
            print("** class doesn't exist **")
        elif len(my_args) < 2:
            print("** instance id missing **")
        elif len(my_args) < 3:
            print("** attribute name missing **")
        elif len(my_args) < 4:
            print("** value missing **")
        else:
            if len(my_args) > 4:
                value = " ".join(my_args[i] for i in range(3, len(my_args)))
            else:
                value = my_args[3]
            obj_dict = models.storage.all()
            for object in obj_dict.values():
                if object.id == my_args[1]:
                    value = self.evaluate_value(value)
                    if isinstance(value, str):
                        value.strip('"')
                    setattr(object, my_args[2], value)
                    models.storage.save()
                    break
            else:
                print("** no instance found **")

    def do_count(self, line):
        """
        Method that retrieve the number of instances
        of a class: <class name>.count().
        """
        if line not in my_classes:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        count = 0
        for key_obj in objects.keys():
            if line in key_obj and line in my_classes:
                count += 1
        print(count)

    @staticmethod
    def evaluate_value(value):
        """
        Evaluates the value and returns its appropriate type.
        """
        if value.startswith('"') and value.endswith('"') and '[' not in value:
            # Remove quotes from string values
            return value.strip('"')
        elif value.startswith("'") and value.endswith("'")\
                and '[' not in value:
            # Remove quotes from string values
            return value.strip("'")
        elif value.isdigit():
            # Convert to integer if it's a number
            return int(value)
        elif "." in value and all(c in "0123456789.-" for c in value):
            # Convert to float if it's a decimal number
            return float(value)
        elif "[" in value and "]" in value:
            # Convert to list if it's a list representation
            try:
                return eval(value.strip('"'))  # Use eval for list conversion
            except TypeError:
                print("** Invalid list format **")
            return None  # Return None to signal an invalid format
        else:
            return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
