Architecture Overview
=====================

This project is designed for PyQtQuick applications with multi-threaded QML UI integration.

Components
----------

* **main.py**: Entry point, initializes the application and threads.

* **Template_Material/**
  
  * **bico_qmutexqueue.py**: Provides a thread-safe queue for inter-thread communication.
  * **bico_quithread.py**: Defines the main thread class with QML UI integration.
  * **bico_qthread.py**: Base class for threads with message queue support.
  * **bico_qmessdata.py**: Defines the message data structure for thread communication.

* **Client_Code/**

  * **Bico_QUIThread_Sample/**

    * **Bico_QUIThread_Sample.py**: Example implementation of a QUIThread for demonstration.
    * **Data_Object/**

      * **Example_Data_Object.py**: Example data object used in the sample thread.

* **resource/**: Handles resource integration for QML files (e.g., icons, QML resources).
* **docs/**: Sphinx documentation sources, including architecture and module references.
* **QML files**: User interface definitions for the application, loaded by threads.
* **requirements.txt**: Lists Python dependencies for the project.
* **README.md**: Project overview and setup instructions.

Thread Communication
--------------------

Threads communicate using :class:`Template_Material.bico_qmutexqueue.Bico_QMutexQueue` and :class:`Template_Material.bico_qmessdata.Bico_QMessData`.

.. uml::

    @startuml
    actor User
    User -> main.py : start application
    main.py -> "Bico_QUIThread A" : create thread
    main.py -> "QML UI A" : create UI
    main.py -> "Bico_QUIThread B" : create thread
    User -> "QML UI A" : Manipulate the UI (click, text input, etc.)
    "QML UI A" -> "Bico_QUIThread A" : send/receive signals
    "Bico_QUIThread A" -> "Bico_QUIThread B" : enqueue/dequeue messages
    "Bico_QUIThread B" -> "Bico_QUIThread A" : enqueue/dequeue messages
    "Bico_QUIThread A" -> "QML UI A" : send/receive signals
    "QML UI A" -> User : Update UI to User
    @enduml