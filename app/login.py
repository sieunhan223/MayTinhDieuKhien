import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QMainWindow, QWidget
from PyQt5.QtCore import Qt
import cua_thong_minh


class LoginWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UIinit()
        
    def UIinit(self):

        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        
        self.central_widget = QWidget()  # Tạo widget trung tâm
        self.setCentralWidget(self.central_widget)  # Đặt widget trung tâm cho QMainWindow
        
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
        self.text1.returnPressed.connect(self.get_info)
        self.fbox.addRow(self.l3,self.text1)
        self.vbox.addLayout(self.fbox)
        
        self.l4 = QLabel("Mật khẩu: ")
        self.f2.setBold(False)
        self.l4.setFont(self.f2)
        self.text2 = QLineEdit()
        self.text2.setEchoMode(QLineEdit.Password)
        self.text2.returnPressed.connect(self.get_info)
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
        
        self.central_widget.setLayout(self.vbox)  # Đặt QVBoxLayout làm layout cho widget trung tâm

        self.setWindowTitle("Hệ thống mở cửa thông minh")
        self.setGeometry(750, 250, 400, 440)
        self.show()

    def get_info(self):
        
        self.username = self.text1.text()  # Lấy nội dung trong textbox
        self.password = self.text2.text()  # Lấy nội dung trong textbox
        print("user: ", self.username)
        print("password: ", self.password)
        if ((self.username == "admin") and self.password == "123456"):
            self.smartdoor = cua_thong_minh.SmartDoor()
            self.hide()
            self.smartdoor.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = LoginWindow()
    sys.exit(app.exec_())
