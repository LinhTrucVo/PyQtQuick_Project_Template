import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

Window {
	id: window
	
	objectName: "window"
    width: 1080
    height: 480
    visible: true
    title: qsTr("Hello World")

    Button {
        objectName: "button"
        id: button
        x: 423
        y: 287
        text: qsTr("main")

		onClicked:
		{
			var data_to_thread
			if (qmess.text == "size")
			{
				// data_to_thread = Qt.size(int(qdata.text), int(qdata.text))
				data_to_thread = Qt.size(Number(qdata.text), Number(qdata.text))
			}
			else
			{
				data_to_thread = qdata.text
			}

			toThread(qmess.text, data_to_thread)
		}
    }

    TextField {
        id: qmess
        x: 205
        y: 149
        width: 318
        height: 40
        placeholderText: qsTr("mess")
    }

    TextField {
        id: qdata
        x: 205
        y: 214
        width: 318
        height: 40
        placeholderText: qsTr("data")
    }

// =====================================================================================================================================================================

	// Terminate the thread when the window is close - begin ------------------------------------------------------------------
	Connections
	{
		target: window
		function onClosing (){ toThread("terminate", "") } // new syntax
	}
	// Terminate the thread when the window is close - begin ------------------------------------------------------------------


// =====================================================================================================================================================================


// Signal handling - begin ------------------------------------------------------------------------------------------------------------------------------------

	// Signal transfer send data - begin ------------------------------------------------------------------
	signal toThread(string rev_mess, var rev_data)
	signal fromThread(string rev_mess, var rev_data)
	// Signal transfer send data - end ------------------------------------------------------------------

	// Handle data from Thread - begin ------------------------------------------------------------------
	onFromThread: function(rev_mess, rev_data)
	{
		// This block of code is allowed to be changed - begin -------------------
		if (rev_mess === "size")
		{
			button.height = rev_data.height
			button.width = rev_data.width
		}
		else
		{
			console.log(rev_mess + " " + rev_data)
		}

		// This block of code is allowed to be changed - end -------------------
	}
	// Handle data from Thread - end ------------------------------------------------------------------

// Signal handling - end ------------------------------------------------------------------------------------------------------------------------------------
}