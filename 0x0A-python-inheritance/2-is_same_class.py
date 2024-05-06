#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if object 'obj' is the instance of the 'a_class'


    Args:
        obj: The object to check
        a_class: The class to compare against


    Returns:
        True if the 'obj' is an instance of 'a_class', False otherwise
    """
    return obj.__class__ is a_class
