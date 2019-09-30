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
        self.__queue = deque(maxlen=self.__max_size)

    def enqueue(self, element):
        """
        Inserts element to the rear of the queue
        :param element: Element to be inserted
        :return: None
        """
        if len(self.__queue) == self.__max_size:
            return error.error_message("Overflow Error", "enqueue(): stack full, cannot insert {}".format(element))
        self.__queue.append(element)

    def deque(self):
        """
        Removes an element from the front of the queue
        :return: Element removed
        """
        if len(self.__queue) == 0:
            return error.error_message("Underflow Error", "dequeue(): queue empty, cannot remove element")
        return self.__queue.pop()


