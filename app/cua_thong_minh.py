
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class SmartDoor(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.UIinit()
    def UIinit(self):
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        f1 = QFont("Arial", 15)
        f1.setBold(True)
        
        self.l1 = QLabel(text="Trạng thái cửa: ")
        self.l1.setFont(f1)
        
        self.status_door = QLabel("Đóng")
        self.status_door.setFixedSize(80,40)
        self.status_door.setStyleSheet("color :red")
        self.status_door.setFont(f1)
        
        self.fbox.addRow(self.l1,self.status_door)
        
        self.l2 = QLabel(f"ID vân tay {self.status_door.text().lower()} cửa: ")
        self.l2.setFont(f1)
        
        self.id = QLabel("1")
        self.id.setFixedSize(80,40)
        self.id.setFont(f1)
        
        self.fbox.addRow(self.l2,self.id)
        
        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)
        
        self.vbox.addLayout(self.fbox)
        
        self.setGeometry(750,250,400,440)
        self.setWindowTitle("Hệ thống mở cửa thông minh")
        self.setLayout(self.vbox)
        self.show()
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = SmartDoor()
    sys.exit(app.exec_())