"""
Main entry point for the PyQtQuick project.

This module initializes the QGuiApplication, sets up the main threads, and loads the QML UI.
"""

import sys
import os
from PySide6.QtGui import QGuiApplication

from Template_Material.bico_qmutexqueue import Bico_QMutexQueue
from Template_Material.bico_quithread import Bico_QUIThread
from Client_Code.Bico_QUIThread_Sample.Bico_QUIThread_Sample import Bico_QUIThread_Sample

current_path = os.getcwd()

import resource.resource

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    Bico_QUIThread.setMainApp(app)

    # Create and start the first thread
    Bico_QUIThread.create(
        Bico_QUIThread_Sample,
        Bico_QMutexQueue(), 
        1, 
        Bico_QMutexQueue(), 
        1, 
        "task_0", 
        os.path.join(current_path, "Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml")
    )
    Bico_QUIThread.getThreadHash()["task_0"].start()
    
    # Create and start the second thread
    Bico_QUIThread.create(
        Bico_QUIThread_Sample,
        Bico_QMutexQueue(), 
        1, 
        Bico_QMutexQueue(), 
        1, 
        "task_1", 
        os.path.join(current_path, "Client_Code/Bico_QUIThread_Sample/Bico_QUIThread_Sample.qml")
    )
    Bico_QUIThread.getThreadHash()["task_1"].start()

    sys.exit(app.exec())