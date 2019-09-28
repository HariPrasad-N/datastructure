from utils import error


# Class to implement functionality of a stack
class Stack:
    def __init__(self, size):
        """
            attributes:
                size -> Max size of the stack before stack overflow.
        """
        self.stack = []
        try:
            self.max_size = int(size)
        except ValueError:
            error.error_message("TypeError", "__init__(): Size argument passed invalid")

    def push(self, element):
        """
        Pushes element to the top of the stack
        :param element: Element to be pushed on the top of the stack
        :return: None
        """
        if len(self.stack) == self.max_size:
            error.error_message("Overflow Error", "push(): Stack full, cannot push {}".format(element))
        self.stack.append(element)

    def pop(self):
        """
        Pop an element from the top of the stack
        :return: Element
        """
        try:
            return self.stack.pop()
        except IndexError:
            error.error_message("Underflow Error", "pop(): Stack empty, cannot pop")

    def peek(self):
        """
        Peeks at the element at the top of the stack. It doesn't remove the element
        :return: Element
        """
        try:
            return self.stack[-1]
        except IndexError:
            error.error_message("Underflow Error", "peek(): Stack empty, cannot peek")

    def empty(self):
        """
        Check if stack is empty.
        :return: Boolean
        """
        return len(self.stack) == 0

    def full(self):
        """
        Check if stack is full
        :return: Boolean
        """
        return len(self.stack) == self.max_size

    def count(self):
        """
        Count number of elements in stack
        :return: Number of elements -> int
        """
        return len(self.stack)

    def reverse(self):
        """
        Reverse the elements in the stack
        :return: None
        """
        reversed(self.stack)

