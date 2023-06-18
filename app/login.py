import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from . import cua_thong_minh


class LoginWindow(QWidget):
    def __init__(self, ser) -> None:
        super().__init__()
        self.ser = ser
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        self.UIinit()
        
    def UIinit(self):


        
        
        self.titleProject = QLabel(text="Hệ Thống Cửa Thông Minh")
        self.titleProject.setStyleSheet("color: red")
        self.f1 = QFont("Airal",17)
        self.f1.setBold(True)
        self.titleProject.setFont(self.f1)
        self.vbox.addWidget(self.titleProject)

        self.titleLogin = QLabel(text="Đăng nhập")
        self.titleLogin.setStyleSheet("color: #f58a42")
        self.f2 = QFont("Airal",15)
        self.f2.setBold(True)
        self.titleLogin.setFont(self.f2)
        self.vbox.addWidget(self.titleLogin)
        self.vbox.setAlignment(self.titleLogin,Qt.AlignCenter)
        
        self.labelUser = QLabel("Tài khoản: ")
        self.f2.setBold(False)
        self.f2.setPixelSize(18)
        self.labelUser.setFont(self.f2)
        self.textUser = QLineEdit()
        
        self.fbox.addRow(self.labelUser,self.textUser)
        
        self.labelPassword = QLabel("Mật khẩu: ")
        self.f2.setBold(False)
        self.labelPassword.setFont(self.f2)
        self.textPassword = QLineEdit()
        self.textPassword.setEchoMode(QLineEdit.Password)
        
        self.fbox.addRow(self.labelPassword,self.textPassword)
        self.vbox.addLayout(self.fbox)
        
        self.but1 = QPushButton(text="Xác nhận")
        self.but1.setStyleSheet("color: #613b0a")
        self.f2.setBold(True)
        self.f2.setPixelSize(15)
        self.but1.setFont(self.f2)
        self.but1.setFixedSize(80,40)
        
        self.vbox.addWidget(self.but1)
        self.vbox.setAlignment(self.but1, Qt.AlignCenter)
        
        self.info = QLabel()
        self.info.setStyleSheet("color: red")
        self.vbox.addWidget(self.info)
        
        self.setLayout(self.vbox) 

        
        
        # self.setWindowTitle("Hệ thống mở cửa thông minh")
        # self.setGeometry(750, 250, 400, 440)
        # self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = LoginWindow()
    my_app.show()
    sys.exit(app.exec_())
