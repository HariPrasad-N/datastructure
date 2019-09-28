from utils import error


# Class to implement functionality of a stack
class Stack:
    def __init__(self, size):
        """
            attributes:
                size -> Max size of the stack before stack overflow.
        """
        self.__stack = []
        try:
            self.__max_size = int(size)
        except ValueError:
            error.error_message("TypeError", "__init__(): Size argument passed invalid")

    def push(self, element):
        """
        Pushes element to the top of the stack
        :param element: Element to be pushed on the top of the stack
        :return: None
        """
        if len(self.__stack) == self.__max_size:
            error.error_message("Overflow Error", "push(): stack full, cannot push {}".format(element))
        self.__stack.append(element)

    def pop(self):
        """
        Pop an element from the top of the stack
        :return: Element
        """
        try:
            return self.__stack.pop()
        except IndexError:
            error.error_message("Underflow Error", "pop(): stack empty, cannot pop")

    def peek(self):
        """
        Peeks at the element at the top of the stack. It doesn't remove the element
        :return: Element
        """
        try:
            return self.__stack[-1]
        except IndexError:
            error.error_message("Underflow Error", "peek(): stack empty, cannot peek")

    def empty(self):
        """
        Check if stack is empty.
        :return: Boolean
        """
        return len(self.__stack) == 0

    def full(self):
        """
        Check if __stack is full
        :return: Boolean
        """
        return len(self.__stack) == self.__max_size

    def count(self):
        """
        Count number of elements in stack
        :return: Number of elements -> int
        """
        return len(self.__stack)

    def reverse(self):
        """
        Reverse the elements in the stack
        :return: None
        """
        self.__stack.reverse()

