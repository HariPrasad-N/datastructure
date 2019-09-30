from utils import error


# Class to implement functionality of a queue
class Queue:
    def __init__(self, size):
        """
            attributes:
                size -> Max size of the queue
        """
        self.__queue = []
        try:
            self.__max_size = int(size)
        except ValueError:
            error.error_message("TypeError", "__init__(): Size argument passed invalid")

    def enqueue(self, element):
        """
        Inserts element to the rear of the queue
        :param element: Element to be inserted
        :return: None
        """
        if len(self.__queue) == self.__max_size:
            error.error_message("Overflow Error", "enqueue(): stack full, cannot insert {}".format(element))
        self.__queue.append(element)
