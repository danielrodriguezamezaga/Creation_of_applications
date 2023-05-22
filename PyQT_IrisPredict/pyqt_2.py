from PyQt5.QtWidgets import *
import sys

def funcion_imprimir():
    print(line_edit_1.text())
    
def funcion_salir():
    ventana.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = QMainWindow()
    ventana.setGeometry(800, 100, 500, 500)

    ventana.setWindowTitle("Mi primera aplicación PyQt")
    label_1 = QLabel(ventana)
    label_1.setText("Aplicación programada con PyQt5")
    label_1.adjustSize()
    label_1.move(150, 20)

    label_2 = QLabel(ventana)
    label_2.setText("Escribe algo en el siguiente QLineEdit: ")
    label_2.adjustSize()
    label_2.move(20, 100)
    
    boton_1 = QPushButton(ventana)
    boton_1.setText("Imprimir en cmd")
    boton_1.clicked.connect(funcion_imprimir)
    boton_1.move(20, 200)

    boton_2 = QPushButton(ventana)
    boton_2.setText("Salir")
    boton_2.clicked.connect(funcion_salir)
    boton_2.move(390, 450)

    line_edit_1 = QLineEdit(ventana)
    line_edit_1.move(20, 150)

    ventana.show()
    sys.exit(app.exec_())
