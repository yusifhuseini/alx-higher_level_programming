#!/usr/bin/python3

"""
A script that creates a Singly linked list
"""


class Node:
    """
    Attributes:
        data (int): object data
        next_node (Node): object of type Node
    """

    def __init__(self, data, next_node=None):
        """
        Args:
            data (int): object data
            next_node (Node): instance of Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns:
            int: object data
        """
        return self.__data

    @property
    def next_node(self):
        """
        Returns:
            Node: instance of Node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Args:
            value (int): object data
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @next_node.setter
    def next_node(self, value):
        """
        Args:
            value (int): instance of Node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        """
        This method sets a private instance attribute, head
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        This method adds a Node class to the linked list in a sorted order

        Args:
            value (int): data for new Node instance
        """
        currentNode = self.__head
        previousNode = None
        if currentNode is None or currentNode.data >= value:
            self.__head = Node(value, currentNode)
        else:
            while currentNode is not None and value > currentNode.data:
                previousNode = currentNode
                currentNode = currentNode.next_node
            previousNode.next_node = Node(value, currentNode)

    def __str__(self):
        """
        String representation of class instance
        """
        string = []
        currentNode = self.__head
        while currentNode is not None:
            string.append(str(currentNode.data))
            currentNode = currentNode.next_node
        if len(string) > 0:
            return '\n'.join(string)
        return ""
