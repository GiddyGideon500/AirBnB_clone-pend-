#!/usr/bin/python3
"""Module console

This Module contains a definition for HBNBCommand Class
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """AirBnB clone console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exist the console using Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """prevents default behavior of cmd to ignore running command on 
        empty line plus enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
