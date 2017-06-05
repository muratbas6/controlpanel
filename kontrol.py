from PyQt5 import QtGui,QtCore,QtWidgets
import sys
import serial

data = serial.Serial('COM7', 9600)


class Pencere(QtWidgets.QWidget):

    def elsalla(self):
        print("HI!")
        data.write(b'a')
    def dab(self):
        print("DAB")


    def keyPressEvent(self, event):
        if self.checkbox1.isChecked():
            if type(event) == QtGui.QKeyEvent:
                key = event.key()
                print(key)
                if key == 87:
                    print("W===> GO AHEAD")
                    data.write(b"w")
                elif key == 83:
                    print("S===> TURN LEFT")
                    data.write(b"l")
                elif key == 65:
                    print("A===> GO BACK")
                    data.write(b"b")
                elif key == 68:
                    print("D===> TURN RIGHT")
                    data.write(b"r")


    def slot_method(self):
        if self.checkbox1.isChecked():
            print("Tiklendi")
            print("Kontrol Klavyede")



    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 130)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("CrawleX")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.checkbox1 = QtWidgets.QCheckBox(self)
        self.checkbox1.setText("Klavye ile kontrol")
        self.checkbox1.setGeometry(10, 5, 100, 13)
        self.checkbox1.toggled.connect(self.slot_method)
        self.checkbox1.toggled.connect(self.keyPressEvent)

        self.butondab = QtWidgets.QPushButton(self)
        self.butondab.setGeometry(130,5,55,20)
        self.butondab.setText("DAB!")
        self.butondab.clicked.connect(self.dab)

        self.butonelsalla = QtWidgets.QPushButton(self)
        self.butonelsalla.setGeometry(130, 30, 55, 20)
        self.butonelsalla.setText("Hi!")
        self.butonelsalla.clicked.connect(self.elsalla)

        self.bilgi = QtWidgets.QLabel(self)
        self.bilgi.setText("github/muratbas6")
        self.bilgi.setGeometry(160,90,100,50)

uygulama = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.show()
uygulama.exec_()