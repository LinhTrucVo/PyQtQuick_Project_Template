from PySide6.QtCore import QMutex
from collections import deque

class Bico_QMutexQueue(deque):
    pass
    def __init__(self, items = []):
        deque.__init__(self, items)
        self._mutex = QMutex()

    def enqueue(self, item):
        self._mutex.lock()
        self.append(item)
        self._mutex.unlock()

    def enqueueToBack(self, item):
        self._mutex.lock()
        self.appendleft(item)
        self._mutex.unlock()
    
    def dequeue(self):
        self._mutex.lock()
        # if data available in queue
        if len(self) > 0:
            item = self.popleft()
            sucessful = 1
        else:
            item = None
            sucessful = 0
        self._mutex.unlock()
        return item, sucessful

    def dequeueFromFront(self):
        self._mutex.lock()
        # if data available in queue
        if len(self) > 0:
            item = self.pop()
            sucessful = 1
        else:
            item = None
            sucessful = 0
        self._mutex.unlock()
        return item, sucessful
