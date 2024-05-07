#!/usr/bin/python3


"""Define a class"""


class MyList(list):
    """
    A custom list class that extends the built-in list class(list)
    """

    def __init__(self, *args):
        """
        Initialize my list instance.

        Args:
            *args: Variable number of elements to initialize the list.
        """

        super().__init__(*args)

    def print_sorted(self):
        """
        print the elements of the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
