"""
Thread-safe queue implementation using QMutex.

Classes
-------
Bico_QMutexQueue
    A thread-safe queue for inter-thread communication.
"""

from PySide6.QtCore import QMutex
from collections import deque

class Bico_QMutexQueue(deque):
    """
    Thread-safe queue using QMutex for synchronization.

    Parameters
    ----------
    items : list, optional
        Initial items for the queue.
    """
    def __init__(self, items = []):
        deque.__init__(self, items)
        self._mutex = QMutex()

    def enqueue(self, item):
        """
        Add an item to the end of the queue.

        Parameters
        ----------
        item : object
            The item to add.
        """
        self._mutex.lock()
        self.append(item)
        self._mutex.unlock()

    def enqueueToBack(self, item):
        """
        Add an item to the front of the queue.

        Parameters
        ----------
        item : object
            The item to add.
        """
        self._mutex.lock()
        self.appendleft(item)
        self._mutex.unlock()
    
    def dequeue(self):
        """
        Remove and return an item from the front of the queue.

        Returns
        -------
        tuple
            (item, successful) where successful is 1 if an item was dequeued, 0 otherwise.
        """
        self._mutex.lock()
        if len(self) > 0:
            item = self.popleft()
            sucessful = 1
        else:
            item = None
            sucessful = 0
        self._mutex.unlock()
        return item, sucessful

    def dequeueFromFront(self):
        """
        Remove and return an item from the back of the queue.

        Returns
        -------
        tuple
            (item, successful) where successful is 1 if an item was dequeued, 0 otherwise.
        """
        self._mutex.lock()
        if len(self) > 0:
            item = self.pop()
            sucessful = 1
        else:
            item = None
            sucessful = 0
        self._mutex.unlock()
        return item, sucessful
