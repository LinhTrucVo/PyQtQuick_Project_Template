"""
Sample implementation of a QUIThread for demonstration.

Classes
-------
Task1
    Example subclass of Bico_QUIThread for handling messages and UI events.
"""

from lib import Bico_QMessData
from lib import Bico_QUIThread
from .Data_Object.Task1_Data import Task1_Data

class Task1(Bico_QUIThread):
    """
    Example subclass of Bico_QUIThread for handling messages and UI events.
    """
    i = 0
    ex_data_obj = Task1_Data()
    def MainTask(self):
        """
        Main task loop for the thread.

        Returns
        -------
        int
            1 to continue, 0 to terminate.
        """
        continue_to_run = 1
        
        i = 0
        input, result = self.qinDequeue()

        if result:
            mess = input.mess()
            data = input.data()
            if (mess == "terminate"):            
                continue_to_run = 0
            elif (mess == "num1"):
                print(self.objectName() + " " + mess + " " + str(self.ex_data_obj.getData_1()))
            elif (mess == "num2"):
                print(self.objectName() + " " + mess + " " + str(self.ex_data_obj.getData_2()))
            elif (mess == "text"):
                print(self.objectName() + " " + mess + " " + data)
                self.toUI.emit(mess, data)
            elif (mess == "size"):
                print(self.objectName() + " " + mess + " " + str(data.width()) + str(data.height()))
                self.toUI.emit(mess, data)
            elif (mess == "from_another_thread"):
                print(self.objectName() + " " + mess + ": "  + input.src() + " - " + str(data))

        print("Hello from " + self.objectName())
        print("Num of running thread: " + str(len(Bico_QUIThread.getThreadHash())))
        self.msleep(100)

        if ((self.objectName() == "task_1") and (Bico_QUIThread.getThreadHash().get("task_0") != None)):
            self.i += 1
            mess_data = Bico_QMessData("from_another_thread", self.i)
            mess_data.setSrc(self.objectName())
            Bico_QUIThread.getThreadHash().get("task_0").qinEnqueue(mess_data)
            # self.msleep(2365)

        return continue_to_run
