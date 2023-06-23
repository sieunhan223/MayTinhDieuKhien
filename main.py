import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QAction
from PyQt5.QtGui import QMovie
from app.login import *
from app.xoa_van_tay import *
from app.them_van_tay import * 
from app.modules import *
from app.cua_thong_minh import *
from app.loading import *

class MySleep(QThread):
    def __init__(self,smartDoor):
        super().__init__()
        self.smartDoor = smartDoor
    def run(self):
        self.smartDoor.set_loading_state()
        self.sleep(2)  # Đặt độ trễ 2 giây (2000 ms)
        # Thực hiện các tác vụ sau độ trễ

class SmartDoor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(750,250,400,440)
        self.setWindowTitle("Hệ thống mở cửa thông minh")

        self.toolbar = self.addToolBar('Công cụ')

        self.toolbar = self.addToolBar('Công cụ')
        self.action1 = QAction('Đăng xuất', self)
        self.action1.triggered.connect(self.switchToWindowLogin)
        self.toolbar.addAction(self.action1)
        self.action2 = QAction('Cửa thông minh', self)
        self.action2.triggered.connect(self.switchToDetails)
        self.toolbar.addAction(self.action2)
        self.action3 = QAction('Tạo vân tay', self)
        self.action3.triggered.connect(self.switchToWindowAdd)
        self.toolbar.addAction(self.action3)
        self.action4 = QAction('Xóa vân tay', self)
        self.action4.triggered.connect(self.switchToWindowDelete)
        self.toolbar.addAction(self.action4)
        
        while True:
            try:
                self.ser = serial.Serial("COM7",9600,write_timeout=2)
                print("da ket noi!")
                break
            except:
                print("ko ket noi dc")
        
        self.central_widget = QWidget()  # Tạo widget trung tâm
        self.setCentralWidget(self.central_widget)

        self.content_layout = QVBoxLayout(self.central_widget)

        self.login = LoginWindow(self.ser)
        self.content_layout.addWidget(self.login)

        self.details = Details(self.ser)
        self.content_layout.addWidget(self.details)
        
        self.add = Add(self.ser)
        self.content_layout.addWidget(self.add)
        
        self.delete = Delete(self.ser)
        self.content_layout.addWidget(self.delete)
        
        self.loadingPage = LoadingWidget()
        self.sleep = MySleep(self)

        self.switchToWindowLogin()

    def switchToWindowLogin(self):
        self.login.but1.clicked.connect(self.get_info)
        self.login.textUser.returnPressed.connect(self.get_info)
        self.login.textPassword.returnPressed.connect(self.get_info)
        self.toolbar.hide()
        self.login.show()
        self.details.hide()
        self.add.hide()
        self.delete.hide()
        self.show()
        
    def switchToDetails(self):
        self.toolbar.show()
        self.login.hide()
        self.details.show()
        self.add.hide()
        self.delete.hide()
        self.show()
    def switchToWindowDelete(self):
        self.toolbar.show()
        self.login.hide()
        self.details.hide()
        self.add.hide()
        self.delete.show()
        self.show()
    def switchToWindowAdd(self):
        self.toolbar.show()
        self.login.hide()
        self.details.hide()
        self.add.show()
        self.delete.hide()
        self.show()
        
    def get_info(self):
        
        self.username = self.login.textUser.text()  # Lấy nội dung trong textbox
        self.password = self.login.textPassword.text()  # Lấy nội dung trong textbox
        print("user: ", self.username)
        print("password: ", self.password)
        if ((self.username == "admin") and self.password == "haha"):
            self.switchToDetails()
        else:
            self.login.info.setText("Sai tài khoản hoặc mật khẩu!")
    def set_loading_state(self):
        self.update_content_widget(self.loadingPage)

    def update_content_widget(self, widget):
        self.setCentralWidget(widget)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = SmartDoor()
    sys.exit(app.exec_())