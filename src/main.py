"""
Main entry point for the PyQtQuick project.

This module initializes the QGuiApplication, sets up the main threads, and loads the QML UI.
"""

import sys
import os
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QDirIterator

from lib import Bico_QMutexQueue
from lib import Bico_QUIThread
from Client_Code.Task1.Task1 import Task1

current_path = os.getcwd()

# Import the qml resource, do not delete this import
import resource.resource

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    Bico_QUIThread.setMainApp(app)
    
    qrc = QDirIterator(":", QDirIterator.Subdirectories)
    while qrc.hasNext():
        print(qrc.next())
#  ------------------------------------------------------------------------------
    Bico_QUIThread.create(
        # # Using pure qml
        # Task1,
        # Bico_QMutexQueue(), 
        # 1, 
        # Bico_QMutexQueue(), 
        # 1, 
        # "task_0", 
        # os.path.join(current_path, "Client_Code/Task1/Task1.qml")
        
        # Using qml which is intergrated to Qt resource
        Task1,
        Bico_QMutexQueue(),
        1, 
        Bico_QMutexQueue(), 
        1, 
        "task_0", 
        ":/Client_Code/Task1/UI/Task1Content/App.qml"
    )
    Bico_QUIThread.getThreadHash()["task_0"].start()
    

    # Bico_QUIThread.create(
    #     # # Using pure qml
    #     # Task1,
    #     # Bico_QMutexQueue(), 
    #     # 1, 
    #     # Bico_QMutexQueue(), 
    #     # 1, 
    #     # "task_0", 
    #     # os.path.join(current_path, "Client_Code/Task1/Task1.qml")
        
    #     # Using qml which is intergrated to Qt resource
    #     Task1,
    #     Bico_QMutexQueue(),
    #     1, 
    #     Bico_QMutexQueue(), 
    #     1, 
    #     "task_1", 
    #     ":/Client_Code/Task1/UI/Task1Content/App.qml"
    # )
    # Bico_QUIThread.getThreadHash()["task_1"].start()
#  ------------------------------------------------------------------------------


    sys.exit(app.exec())
