from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

if __name__ == "__main__":
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec_()

