from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout
from PyQt5.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.UIinit()
    def UIinit(self):
        
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        
        self.l1 = QLabel(text="Hệ Thống Cửa Thông Minh")
        self.l1.setStyleSheet("color: red")
        self.f1 = QFont("Airal",17)
        self.f1.setBold(True)
        self.l1.setFont(self.f1)
        self.vbox.addWidget(self.l1)

        self.l2 = QLabel(text="Đăng nhập")
        self.l2.setStyleSheet("color: #f58a42")
        self.f2 = QFont("Airal",15)
        self.f2.setBold(True)
        self.l2.setFont(self.f2)
        self.vbox.addWidget(self.l2)
        self.vbox.setAlignment(self.l2,Qt.AlignCenter)
        
        self.l3 = QLabel("Tài khoản: ")
        self.f2.setBold(False)
        self.f2.setPixelSize(18)
        self.l3.setFont(self.f2)
        self.text1 = QLineEdit()
        self.fbox.addRow(self.l3,self.text1)
        self.vbox.addLayout(self.fbox)
        
        self.l4 = QLabel("Mật khẩu: ")
        self.f2.setBold(False)
        self.l4.setFont(self.f2)
        self.text2 = QLineEdit()
        self.text2.setEchoMode(QLineEdit.Password)
        self.fbox.addRow(self.l4,self.text2)
        self.vbox.addLayout(self.fbox)
        
        self.but1 = QPushButton(text="Xác nhận")
        self.but1.setStyleSheet("color: #613b0a")
        self.f2.setBold(True)
        self.f2.setPixelSize(15)
        self.but1.setFont(self.f2)
        self.but1.setFixedSize(80,40)
        self.but1.clicked.connect(self.get_info)
        self.vbox.addWidget(self.but1)
        self.vbox.setAlignment(self.but1, Qt.AlignCenter)
        
        
        self.setGeometry(750,250,400,440)
        self.setWindowTitle("Hệ thống mở cửa thông minh")
        self.setLayout(self.vbox)
        self.show()
    def get_info(self):
        self.input_text1 = self.text1.text()  # Lấy nội dung trong textbox
        self.input_text2 = self.text2.text()  # Lấy nội dung trong textbox
        print("user: ", self.input_text1)
        print("password: ", self.input_text2)


