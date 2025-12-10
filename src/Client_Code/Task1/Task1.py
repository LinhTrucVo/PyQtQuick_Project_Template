"""
Sample implementation of a QUIThread for demonstration.

Classes
-------
Task1
    Example subclass of Bico_QUIThread for handling messages and UI events.
"""

import random
from lib import Bico_QMessData
from lib import Bico_QUIThread
from lib import Bico_QMutexQueue
from .Data_Object.Task1_Data import Task1_Data

class Task1(Bico_QUIThread):
    """
    Example subclass of Bico_QUIThread for handling messages and UI events.
    """
    i = 0
    ex_data_obj = Task1_Data()

    def __init__(self, qin=None, qin_owner=0, qout=None, qout_owner=0, obj_name="", ui_path="", parent=None):
        """
        Initialize Task1 with a list to track child threads.
        """
        super().__init__(qin, qin_owner, qout, qout_owner, obj_name, ui_path, parent)
        self.child_threads = []

    def __del__(self):
        """
        Destructor with custom cleanup logic.
        """
        # Clean up child threads by sending terminate message
        for child_name in self.child_threads:
            thread = Bico_QUIThread.getThreadHash().get(child_name)
            if thread is not None:
                mess_data = Bico_QMessData("terminate", "")
                thread.qinEnqueue(mess_data)
        
        # Call parent destructor if it exists
        if hasattr(super(), '__del__'):
            super().__del__()
            
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
            elif (mess == "create"):
                print(self.objectName() + " " + mess + " " + data)
                random_id = random.randint(1000,9999)
                thread_name = "subtask_"+str(random_id)
                Bico_QUIThread.create(
                    # Using qml which is intergrated to Qt resource
                    Task1,
                    Bico_QMutexQueue(),
                    1, 
                    Bico_QMutexQueue(), 
                    1, 
                    thread_name, 
                    "qrc:/Client_Code/Task1/UI/Task1Content/App.qml"
                )
                Bico_QUIThread.getThreadHash()[thread_name].start()
            elif (mess == "create_child"):
                print(self.objectName() + " " + mess + " " + data)
                random_id = random.randint(1000,9999)
                thread_name = "subtask_"+str(random_id)
                Bico_QUIThread.create(
                    # Using qml which is intergrated to Qt resource
                    Task1,
                    Bico_QMutexQueue(),
                    1, 
                    Bico_QMutexQueue(), 
                    1, 
                    thread_name, 
                    "qrc:/Client_Code/Task1/UI/Task1Content/App.qml"
                )
                Bico_QUIThread.getThreadHash()[thread_name].start()
                # Add child thread to the list for cleanup
                self.child_threads.append(thread_name)
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