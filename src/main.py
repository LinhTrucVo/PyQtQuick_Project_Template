"""
Main entry point for the PyQtQuick project.

This module initializes the QGuiApplication, sets up the main threads, and loads the QML UI.
"""

import sys
import os
from PySide6.QtGui import QGuiApplication

from lib.PyQtLib_Project_Template.src.bico_qmutexqueue import Bico_QMutexQueue
from lib.bico_quithread import Bico_QUIThread
from Client_Code.Bico_QUIThread_Sample.Bico_QUIThread_Sample import Bico_QUIThread_Sample

current_path = os.getcwd()

import resource.resource

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    Bico_QUIThread.setMainApp(app)

    Bico_QUIThread.create(
        # # Using pure qml
        # Bico_QUIThread_Sample,
        # Bico_QMutexQueue(), 
        # 1, 
        # Bico_QMutexQueue(), 
        # 1, 
        # "task_0", 
        # os.path.join(current_path, "Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml")
        
        # Using qml which is intergrated to Qt resource
        Bico_QUIThread_Sample,
        Bico_QMutexQueue(),
        1, 
        Bico_QMutexQueue(), 
        1, 
        "task_0", 
        ":/Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml"
    )
    Bico_QUIThread.getThreadHash()["task_0"].start()
    

    Bico_QUIThread.create(
        # # Using pure qml
        # Bico_QUIThread_Sample,
        # Bico_QMutexQueue(), 
        # 1, 
        # Bico_QMutexQueue(), 
        # 1, 
        # "task_0", 
        # os.path.join(current_path, "Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml")
        
        # Using qml which is intergrated to Qt resource
        Bico_QUIThread_Sample,
        Bico_QMutexQueue(),
        1, 
        Bico_QMutexQueue(), 
        1, 
        "task_1", 
        ":/Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml"
    )
    Bico_QUIThread.getThreadHash()["task_1"].start()

    sys.exit(app.exec())
