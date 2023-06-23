import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QVBoxLayout
from PyQt5.QtCore import  Qt

class Details(QWidget):
    def __init__(self, ser) -> None:
        super().__init__()
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        self.ser = ser
        self.UIinit()

    def UIinit(self):
        #Tạo font
        self.f2 = QFont("Arial", 15)
        self.f2.setBold(True)
        #Trạng thái cửa
        self.labelStatusDoor = QLabel(text="Trạng thái cửa: ")
        self.labelStatusDoor.setFont(self.f2)
        self.statusDoor = QLabel("Đóng")
        self.statusDoor.setFixedSize(80,40)
        self.statusDoor.setStyleSheet("color :red")
        self.statusDoor.setFont(self.f2)
        self.fbox.addRow(self.labelStatusDoor,self.statusDoor)
        #ID
        self.labelDetailIdDoor = QLabel("ID: ")
        self.labelDetailIdDoor.setFont(self.f2)
        self.id = QLabel("None")
        self.id.setFixedSize(80,40)
        self.id.setFont(self.f2)
        self.fbox.addRow(self.labelDetailIdDoor,self.id)
        
        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)
        
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.fbox)
                
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = Details()
    my_app.show()
    sys.exit(app.exec_())