from utils import error
from collections import deque


# Class to implement functionality of a queue
class Queue:
    def __init__(self, size):
        """
            attributes:
                size -> Max size of the queue
        """
        try:
            self.__max_size = int(size)
        except ValueError:
            error.error_message("TypeError", "__init__(): Size argument passed invalid")
            return
        self.__queue = deque(maxlen=self.__max_size)

    def enqueue(self, element):
        """
        Inserts element to the rear of the queue
        :param element: Element to be inserted
        :return: None
        """
        if self.__full():
            return error.error_message("Overflow Error", "enqueue(): stack full, cannot insert {}".format(element))
        self.__queue.append(element)

    def deque(self):
        """
        Removes an element from the front of the queue
        :return: Element removed
        """
        if self.__empty():
            return error.error_message("Underflow Error", "dequeue(): queue empty, cannot remove element")
        return self.__queue.popleft()

    def peek(self):
        """
        Peek an element without actually removing it from the queue
        :return: The element at the front of the queue
        """
        if self.__empty():
            return error.error_message("Underflow Error", "peek(): queue empty, cannot peek")
        return self.__queue[0]

    def __empty(self):
        """
        Check whether the queue is empty
        :return: Boolean
        """
        return len(self.__queue) == 0

    def __full(self):
        """
        Check whether the queue is full
        :return: Boolean
        """
        return len(self.__queue) == self.__max_size

    def display(self):
        """
        Display elements in the queue
        :return: None
        """
        if not self.__empty():
            print("F", end="->")
            for index in range(len(self.__queue)):
                print(self.__queue[index], end="->")
            print("R")
        return

    def reverse(self):
        """
        Reverse the elements in the queue, or switch the front and rear of the queue
        :return: None
        """
        self.__queue.reverse()

    def count(self):
        """
        Count the number of elements in the queue
        :return: Count
        """
        return len(self.__queue)
