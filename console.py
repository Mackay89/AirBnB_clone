#!/usr/bin/python3
"""
Defines the module for console.
"""
import cmd
import re
import shlex
from shlex import split
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


def split_curly_braces(arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)

    if curly_braces:
        id_with_comma = shlex.split(arg[:curly_braces.span()[0]])
        id = [i.strip(",") for i in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = arg.split(",")
        if commands:
            try:
                id = command[0]
            except Exception:
                return "",""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"


class HBNBCommand(cmd.Cmd):
    """
    Defines the HBNBCommand console class.
    """
    prompt = "(hbnb)"
    valid_classes = {
            "BaseModel",
            "User",
            "Amenity",
            "Place",
            "Review",
            "State",
            "City",
            }

    def emptyline(self):
        """
        Do nothing upon receiving an empty line.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        return True
    def do_create(self,arg):
        """
        Usage: create <class_name>
        Create a new instance of BaseModel and save it to JSON file.
        """
        commands = shlex.split(arg)


        if len(comands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class does't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)


    def do_show(self, arg):
        """
        show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        if commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()


            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """
        Usage: destroy <class_name> <id>
        It delete an instance base on the class name and id.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.sve()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Usage: <class name>.count()
        Counts and retrieves the number of instances of a class.
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ ==cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """

        commands = shlex.split(arg)


        if len(commands) == 0:
                print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curl_braces = re.search(r"\{(.*?)\}", arg)

                if curly_braces:
                    try:
                        str_data = curly_braces.group(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        try:
                            attr_names1 = attribute_names[0]
                            attr_values1 = attribute_values[0]
                            setattr(obj, attr_names1, attr_values1)
                        except Exception:
                            pass
                        try:
                            attr_names2 = attribute_names[1]
                            attr_values2 = attribute_values[1]
                            setattr(obj, attr_names2, attr_values2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    
                    attr_name = commands[2]
                    attr_value = commands[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                    obj.save()

    def deefault(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        cls_nm = arg_list[0] # incoming class name

        command = arg_list[1].split('(')

        cmd_met = command[1].split(')')[0] #extra arguments

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met]("{} {}".format(cls_nm, e_arg))
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    obj_id,arg_dict = split_curly_braces(arg)
                except Exception as e:
                    print("Error:", e)
                    return
                try:
                    call = method_dict[cmd_met]
                    return call("{} {} {}".format(cls_nm, obj_id, arg_dict))
                except KeyError:
                    print("** invalid command **")
                except Exception as e:
                    print("Error:", e)
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
