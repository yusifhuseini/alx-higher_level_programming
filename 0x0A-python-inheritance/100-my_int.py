#!/usr/bin/python3

"""
A module: Defines a class that inherits from 'int'
"""


class MyInt(int):
    """
    Inherits `int` and reverses the equality operators
    """
    def __eq__(self, other):
        """
        Inverts the conventional equality operation

        Args:
            self (MyInt): left operand
            other (MyInt): right operand

        Returns:
            boolean: True if left and right operands are different else False
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Inverts the conventional equality operation

        Args:
            self (MyInt): left operand
            other (MyInt): right operand

        Returns:
            boolean: True if left and right operands are equal else False
        """
        return not super().__ne__(other)
