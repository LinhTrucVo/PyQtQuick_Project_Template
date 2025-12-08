"""
Thread class integrating QThread and QML UI.

Classes
-------
Bico_QUIThread
    Thread class for running tasks with QML UI integration.
"""

from PySide6.QtCore import QObject, QThread, QMutex, Signal, Slot, QMetaObject, Qt, Q_ARG
from PySide6.QtQml import QQmlApplicationEngine

from .PyQtLib_Project_Template import Bico_QThread
from .PyQtLib_Project_Template import Bico_QMessData

class EngineLoader(QObject):
    def __init__(self):
        super().__init__()
    
    @Slot('QObject*', str, 'QThread::Priority')
    def createEngine(self, thread, ui_path, priority):
        thread._engine = QQmlApplicationEngine()
        thread._engine.load(ui_path)

        if thread._engine.rootObjects():
            root = thread._engine.rootObjects()[0]

            root.toThread.connect(thread.fromUI, Qt.QueuedConnection)
            thread.toUI.connect(root.fromThread, Qt.QueuedConnection)
        else:
            thread._engine = None

        QThread.start(thread, priority)

engine_loader = EngineLoader()

class Bico_QUIThread(QThread, Bico_QThread):
    """
    Thread class with QML UI integration and message queue support.

    Attributes
    ----------
    thread_hash : dict
        Stores all running threads.
    main_app : QGuiApplication
        Reference to the main application.
    toUI : Signal
        Signal to send data to UI.
    """
    thread_hash = {}
    thread_hash_mutex = QMutex()
    main_app = None
    toUI = Signal(str, "QVariant")

    def __init__(self, qin=None, qin_owner=0, qout=None, qout_owner=0, obj_name="", ui_path="", parent=None):
        """
        Initialize the thread.

        Parameters
        ----------
        qin : Bico_QMutexQueue
            Input queue.
        qin_owner : int
            Ownership flag for input queue.
        qout : Bico_QMutexQueue
            Output queue.
        qout_owner : int
            Ownership flag for output queue.
        obj_name : str
            Name of the thread object.
        ui_path : str
            Path to the QML UI file.
        parent : QObject
            Parent object.
        """
        QThread.__init__(self, parent)
        Bico_QThread.__init__(self, qin, qin_owner, qout, qout_owner)
        self.setObjectName(obj_name)
        __class__.thread_hash_mutex.lock()
        __class__.thread_hash[obj_name] = self
        __class__.thread_hash_mutex.unlock()
        self._ui_path = ui_path
        self._engine = None
        self.finished.connect(lambda: __class__.selfRemove(obj_name))

        # Move this thread object to the main thread for proper signal handling
        # without this, the connection from thread to UI in EngineLoader.createEngine will not work
        if __class__.main_app is not None:
            self.moveToThread(__class__.main_app.thread())
        
    def __del__(self):
        """
        Destructor. Exits the application if no threads remain.
        """
        if not __class__.thread_hash:
            if not (__class__.main_app == None):
                __class__.main_app.exit(0)

    def start(self, priority=QThread.InheritPriority):
        """
        Start the thread and load the QML UI if specified.

        Parameters
        ----------
        priority : QThread.Priority
            Thread priority.
        """
        if (self._ui_path != None) and (self._ui_path != ""):
            # qrc = QDirIterator(":", QDirIterator.Subdirectories)
            # while qrc.hasNext():
            #     self._engine.addImportPath(qrc.next())

            # Can not create QQmlApplicationEngine directly if this "start" func
            # is called by worker Thread (not main thread), because
            # QQmlApplicationEngine must be created in main thread.
            # That why using QMetaObject.invokeMethod to call createEngine
            # which is a slot in EngineLoader object living in main thread (globally).
            QMetaObject.invokeMethod(
                engine_loader,              # object in main thread
                "createEngine",         # method to call (must be slot or invokable)
                Qt.QueuedConnection,    # don't know why QueuedConnection, but if using Direct and Blocking option, the software will be freezed not response
                Q_ARG("QObject*", self),    # pass thread object
                Q_ARG(str, self._ui_path),  # pass UI path
                Q_ARG("QThread::Priority", priority)  # pass priority enum
            )
        else:
            QThread.start(self, priority)

    def MainTask(self):
        """
        Virtual method to be implemented in subclasses.

        Returns
        -------
        int
            0 to stop the thread, 1 to continue.
        """
        return 0

    def run(self):
        """
        Main thread loop.
        """
        while True:
            if(not self.MainTask()):
                break

    def create(custom_class=None, qin=None, qin_owner=0, qout=None, qout_owner=0, obj_name="", ui_path="", parent=None):
        """
        Create a new thread if not already existing.

        Returns
        -------
        Bico_QUIThread or None
        """
        if (__class__.thread_hash.get(obj_name) == None):
            return custom_class(qin, qin_owner, qout, qout_owner, obj_name, ui_path, parent)
        else:
            return None

    def remove(obj_name=""):
        """
        Request removal of a thread by name.

        Returns
        -------
        int
            1 if removed, 0 otherwise.
        """
        if (__class__.thread_hash.get(obj_name) != None):
            mess_data = Bico_QMessData("terminate", "")
            __class__.thread_hash[obj_name].qinEnqueue(mess_data)
            return 1
        return 0

    def getThreadHash():
        """
        Get the dictionary of running threads.

        Returns
        -------
        dict
        """
        return __class__.thread_hash

    def getMainApp():
        """
        Get the main application instance.

        Returns
        -------
        QGuiApplication
        """
        return __class__.main_app

    def setMainApp(app):
        """
        Set the main application instance.

        Parameters
        ----------
        app : QGuiApplication
        """
        __class__.main_app = app

    @Slot(str)
    def selfRemove(obj_name):
        """
        Remove a thread from the thread hash.

        Parameters
        ----------
        obj_name : str
        """
        __class__.thread_hash_mutex.lock()
        __class__.thread_hash.pop(obj_name)
        __class__.thread_hash_mutex.unlock()

    @Slot(str, "QVariant")
    def fromUI(self, mess, data):
        """
        Receive data from the UI.

        Parameters
        ----------
        mess : str
        data : object
        """
        mess_data = Bico_QMessData()
        mess_data.setMess(mess)
        mess_data.setData(data)
        self.qinEnqueue(mess_data)
