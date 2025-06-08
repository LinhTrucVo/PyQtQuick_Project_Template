"""
Message data object for inter-thread communication.

Classes
-------
Bico_QMessData
    Data structure for passing messages and data between threads.
"""

class Bico_QMessData:
    """
    Data structure for passing messages and data between threads.

    Parameters
    ----------
    *args : tuple
        Can be (mess, data) or (src, dst, mess, data).
    """
    def __init__(self, *args):
        if(len(args) == 2):
            self._src = ""
            self._dst = ""
            self._mess = args[0]
            self._data = args[1]
        elif(len(args) == 4):
            self._src = args[0]
            self._dst = args[1]
            self._mess = args[2]
            self._data = args[3]
        else:
            self._src = ""
            self._dst = ""
            self._mess = ""
            self._data = ""
    
    def src(self):
        """
        Get the source.

        Returns
        -------
        str
        """
        return self._src
    def setSrc(self, src):
        """
        Set the source.

        Parameters
        ----------
        src : str
        """
        self._src = src

    def dst(self):
        """
        Get the destination.

        Returns
        -------
        str
        """
        return self._dst
    def setDst(self, dst):
        """
        Set the destination.

        Parameters
        ----------
        dst : str
        """
        self._dst = dst

    def mess(self):
        """
        Get the message.

        Returns
        -------
        str
        """
        return self._mess
    def setMess(self, mess):
        """
        Set the message.

        Parameters
        ----------
        mess : str
        """
        self._mess = mess
        
    def data(self):
        """
        Get the data.

        Returns
        -------
        object
        """
        return self._data
    def setData(self, data):
        """
        Set the data.

        Parameters
        ----------
        data : object
        """
        self._data = data

    def __str__(self):
        """
        String representation.

        Returns
        -------
        str
        """
        return "Bico_QMessData{src: " + self.src() + ", dst: " + self.dst() + ", mess: " + self.mess() + ", data: " + str(self.data()) + "}"
