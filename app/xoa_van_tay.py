import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout, QMainWindow
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
        self.textDetailIdDelete.returnPressed.connect(self.get_id)
        self.textDetailIdDelete.setFixedSize(70,30)
        
        self.fbox.addRow(self.labelDetailIdDelete, self.textDetailIdDelete)

        
        self.but = QPushButton("Gửi", self)
        self.but.move(150,250)
        self.but.setFont(self.f2)
        self.but.setFixedSize(80, 40)
        self.but.clicked.connect(self.get_id)

        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)

        self.vbox.addLayout(self.fbox)
        self.setLayout(self.vbox)
        # self.setGeometry(750, 250, 400, 440)
        # self.setWindowTitle("Hệ thống mở cửa thông minh")
        # self.central_widget.setLayout(self.vbox)
        # self.show()
        
    def get_id(self):
        self.idDelete = self.textDetailIdDelete.text()
        self.ser.write(b"")
        print (self.idDelete)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Delete()
    my_app.show()
    sys.exit(app.exec_())
