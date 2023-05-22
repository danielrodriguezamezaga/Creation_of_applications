from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setGeometry(800, 100, 500, 500)
    ventana.setWindowTitle("QSS Aplicado a varios elementos")
    ventana.setStyleSheet("background-color: grey;")
    
    # boton
    boton_1 = QPushButton("boton_1", ventana)
    boton_1.move(100, 100)
    
    boton_2 = QPushButton("boton_2", ventana)
    boton_2.move(100, 200)
    
    boton_3 = QPushButton("boton_3", ventana)
    boton_3.setStyleSheet("background-color: green; color: white;")
    boton_3.move(100, 300)
    
    estilos = """QPushButton {
        background-color: grey;
        color: black;
        border-width: 5px;
        border-style: solid;
        border-radius: 5;
        padding: 2px;
    }
    """
    
    QApplication.instance().setStyleSheet(estilos)
    ventana.show()
    sys.exit(app.exec_())
    
    