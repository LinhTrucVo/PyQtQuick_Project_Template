Architecture Overview
=====================

This project is designed for PyQtQuick applications with multi-threaded QML UI integration.

Components
----------

* **main.py**: Entry point, initializes the application and threads.
* **Template_Material**: Contains reusable thread, queue, and message data classes.
* **Client_Code**: Example implementation of a threaded QML UI.
* **resource**: Handles resource integration for QML files.

Thread Communication
--------------------

Threads communicate using :class:`Template_Material.bico_qmutexqueue.Bico_QMutexQueue` and :class:`Template_Material.bico_qmessdata.Bico_QMessData`.

.. uml::

   @startuml
   actor User
   User -> main.py : start application
   main.py -> Bico_QUIThread : create thread
   Bico_QUIThread -> Bico_QMutexQueue : enqueue/dequeue messages
   Bico_QUIThread -> QML UI : send/receive signals
   @enduml
