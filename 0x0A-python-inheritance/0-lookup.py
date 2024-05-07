#!/usr/bin/python3

def lookup(obj):
    """Return a list of available attribute and methods of an objects.

    Parameters:
    obj (object): The object to which will retrieve methods and attributes.

    Return:
    List: A list containing a name attributes and methods.
    """
    return [attribute for attribute in dir(obj)]
