"""
Base thread class for message queue communication.

Classes
-------
Bico_QThread
    Base class for threads with input/output message queues.
"""

from Template_Material.bico_qmessdata import Bico_QMessData
from Template_Material.bico_qmutexqueue import Bico_QMutexQueue

class Bico_QThread:
    """
    Base thread class with input/output message queues.

    Parameters
    ----------
    qin : Bico_QMutexQueue, optional
        Input queue.
    qin_owner : bool, optional
        Ownership flag for input queue.
    qout : Bico_QMutexQueue, optional
        Output queue.
    qout_owner : bool, optional
        Ownership flag for output queue.
    """
    def __init__(self, qin:Bico_QMutexQueue = None, qin_owner:bool = False, qout:Bico_QMutexQueue = None, qout_owner:bool = False):
        self._qin = qin
        self._qin_owner = qin_owner
        self._qout = qout
        self._qout_owner = qout_owner

    def qin(self) -> Bico_QMutexQueue:
        """
        Get the input queue.

        Returns
        -------
        Bico_QMutexQueue
        """
        return self._qin

    def setQin(self, qin:Bico_QMutexQueue):
        """
        Set the input queue.

        Parameters
        ----------
        qin : Bico_QMutexQueue
        """
        self._qin = qin
    
    def qout(self) -> Bico_QMutexQueue:
        """
        Get the output queue.

        Returns
        -------
        Bico_QMutexQueue
        """
        return self._qout

    def setQin(self, qout:Bico_QMutexQueue):
        """
        Set the output queue.

        Parameters
        ----------
        qout : Bico_QMutexQueue
        """
        self._qout = qout

    def qinEnqueue(self, item):
        """
        Enqueue an item to the input queue.

        Returns
        -------
        int
            1 if successful, 0 otherwise.
        """
        if not (self._qin == None):
            self._qin.enqueue(item)
            return 1
        return 0

    def qinEnqueueToBack(self, item):
        """
        Enqueue an item to the back of the input queue.

        Returns
        -------
        int
            1 if successful, 0 otherwise.
        """
        if not (self._qin == None):
            self._qin.enqueueToBack(item)
            return 1
        return 0

    def qinDequeue(self):
        """
        Dequeue an item from the input queue.

        Returns
        -------
        tuple
            (item, successful)
        """
        if not (self._qin == None):
            return self._qin.dequeue()
        return None, 0

    def qinDequeueFromFront(self):
        """
        Dequeue an item from the front of the input queue.

        Returns
        -------
        tuple
            (item, successful)
        """
        if not (self._qin == None):
            return self._qin.dequeueFromFront()
        return None, 0

    def qoutEnqueue(self, item):
        """
        Enqueue an item to the output queue.

        Returns
        -------
        int
            1 if successful, 0 otherwise.
        """
        if not (self._qout == None):
            self._qout.enqueue(item)
            return 1
        return 0

    def qoutEnqueueToBack(self, item):
        """
        Enqueue an item to the back of the output queue.

        Returns
        -------
        int
            1 if successful, 0 otherwise.
        """
        if not (self._qout == None):
            self._qout.enqueueToBack(item)
            return 1
        return 0
