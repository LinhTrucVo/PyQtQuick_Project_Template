"""
Sample implementation of a QUIThread for demonstration.

Classes
-------
Bico_QUIThread_Sample
    Example subclass of Bico_QUIThread for handling messages and UI events.
"""

import sys, os

current_path = os.getcwd()

from PySide6.QtGui import QGuiApplication

from PyQtLib_Project_Template.src.bico_qmessdata import Bico_QMessData
from PyQtLib_Project_Template.src.bico_qmutexqueue import Bico_QMutexQueue
from PyQtLib_Project_Template.src.bico_quithread import Bico_QUIThread
from Client_Code.Bico_QUIThread_Sample.Data_Object.Example_Data_Object import Example_Data_Object

class Bico_QUIThread_Sample(Bico_QUIThread):
    """
    Example subclass of Bico_QUIThread for handling messages and UI events.
    """
    i = 0
    ex_data_obj = Example_Data_Object()
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
