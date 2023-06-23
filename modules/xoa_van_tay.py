import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class Delete(QWidget):
    def __init__(self, ser): 
        super().__init__()
        self.ser = ser
        self.UIInit()

    def UIInit(self):
        
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()

        self.f2 = QFont("Arial", 15)
        self.f2.setBold(True)
        self.labelDetailIdDelete = QLabel("Nhập ID vân tay xóa: ")
        self.labelDetailIdDelete.setFont(self.f2)
        
        self.textDetailIdDelete = QLineEdit()
        self.textDetailIdDelete.setFixedSize(70,30)
        
        self.fbox.addRow(self.labelDetailIdDelete, self.textDetailIdDelete)

        self.but = QPushButton("Gửi", self)
        self.but.move(150,250)
        self.but.setFont(self.f2)
        self.but.setFixedSize(80, 40)
        
        # self.desc = QLabel("78687")
        # self.desc.setStyleSheet("color: red")

        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)

        self.vbox.addLayout(self.fbox)
        self.vbox.addWidget(self.but)
        # self.vbox.addWidget(self.desc)
        
        self.setLayout(self.vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Delete()
    my_app.show()
    sys.exit(app.exec_())
