#!/usr/bin/python3

''' Deefines  class 'Node' '''


class Node:
    ''' Initializes the class Node '''

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    ''' Gets/setss the current value of data '''
    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    ''' Gets/sets the current value of next_node '''
    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' Initializes the class '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        ''' initializes a newnode with the current value of 'value' '''
        newnode = Node(value)

        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            newnode.next_node = tmp.next_node
            tmp.next_node = newnode

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
