import sys
import os
current_path = os.getcwd()

from PySide6.QtCore import QThread, QMutex, Signal, Slot
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

from Template_Material.bico_qthread import Bico_QThread
from Template_Material.bico_qmutexqueue import Bico_QMutexQueue
from Template_Material.bico_qmessdata import Bico_QMessData


class Bico_QUIThread(QThread, Bico_QThread):
    thread_hash = {}
    thread_hash_mutex = QMutex()
    main_app = None
    toUI = Signal(str, "QVariant")
    
    x = 0

    def __init__(self, qin=None, qin_owner=0, qout=None, qout_owner=0, obj_name="", ui_path="", parent=None):
        QThread.__init__(self, parent)
        Bico_QThread.__init__(self, qin, qin_owner, qout, qout_owner)
        self.setObjectName(obj_name)
        __class__.thread_hash_mutex.lock()
        __class__.thread_hash[obj_name] = self
        __class__.thread_hash_mutex.unlock()
        self._ui_path = ui_path
        self.finished.connect(lambda: __class__.selfRemove(obj_name))
        __class__.x = 5
        
    def __del__(self):
        if not __class__.thread_hash:
            if not (__class__.main_app == None):
                __class__.main_app.exit(0)

    def start(self, priority=QThread.InheritPriority):
        if (self._ui_path != "") and (self._ui_path != None):
            self._engine = QQmlApplicationEngine()
            self._engine.load(self._ui_path)
            self.toUI.connect(self._engine.rootObjects()[0].fromThread)
            self._engine.rootObjects()[0].toThread.connect(self.fromUI)
        QThread.start(self, priority)

    # Virtual method which will be implemented in the subclass
    def MainTask(self):
        return 0

    def run(self):
        while True:
            if(not self.MainTask()):
                break

    def create(custom_class=None, qin=None, qin_owner=0, qout=None, qout_owner=0, obj_name="", ui_path="", parent=None):
        if (__class__.thread_hash.get(obj_name) == None):
            return custom_class(qin, qin_owner, qout, qout_owner, obj_name, ui_path, parent)
        else:
            return None

    def remove(obj_name=""):
        if (__class__.thread_hash.get(obj_name) != None):
            mess_data = Bico_QMessData("terminate", "")
            __class__.thread_hash[obj_name].qinEnqueue(mess_data)
            return 1
        return 0

    def getThreadHash():
        return __class__.thread_hash

    def getMainApp():
        return __class__.main_app

    def setMainApp(app):
        __class__.main_app = app

    @Slot(str)
    def selfRemove(obj_name):
        __class__.thread_hash_mutex.lock()
        __class__.thread_hash.pop(obj_name)
        __class__.thread_hash_mutex.unlock()

    @Slot(str, "QVariant")
    def fromUI(self, mess, data):
        mess_data = Bico_QMessData()
        mess_data.setMess(mess)
        mess_data.setData(data)
        self.qinEnqueue(mess_data)
        