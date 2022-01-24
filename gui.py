from PyQt5 import QtWidgets, uic,QtGui
import sys
import  server
import asyncio
import threading

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'startServer') # Find the button
        self.list_view = self.findChild(QtWidgets.QListView,"listView")
        self.button.clicked.connect(self.start_server)
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.show()


    def start_server(self):
        # This is executed when the button is pressed
        self.s = threading.Thread(target=server.start_server, args=(self.model,))
        self.s.setDaemon(True)
        self.s.start()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()