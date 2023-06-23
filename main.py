import sys, serial, queue
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QAction
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from modules.login import *
from modules.xoa_van_tay import *
from modules.them_van_tay import * 
from modules.cua_thong_minh import *
from modules.loading import *

class InputThread(QThread):
    def __init__(self, ser) -> None:
        super().__init__()
        self.ser = ser
        
    input = pyqtSignal(str)
    
    def run(self):
        while True:
            if self.ser.in_waiting  > 0:
                try:
                    key = self.ser.readline().decode().strip()
                    self.input.emit(key)
                except:
                    print("loi")

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
        self.add.but.clicked.connect(lambda : self.put_id(self.add))
        
        self.delete = Delete(self.ser)
        self.content_layout.addWidget(self.delete)
        self.delete.but.clicked.connect(lambda : self.put_id(self.delete))
        
        self.loadingPage = LoadingWidget()
        self.content_layout.addWidget(self.loadingPage)
        
        self.timer = QTimer()
        self.queueMain = queue.Queue()
        self.mainData = ""

        #Thực hiện xử lý hiển thị
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start()
        self.threadInput = InputThread(self.ser)
        self.threadInput.input.connect(self.processInput)
        self.threadInput.start()
        
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
        self.loadingPage.hide()
        self.show()
        
    def switchToDetails(self):
        self.loadingPage.details.hide()
        self.set_loading_state()
        QTimer.singleShot(1000, self.DetailsON)
    def switchToWindowDelete(self):
        self.ser.write(b'r')
        self.loadingPage.details.setText("Vui lòng xác thực vân tay trong vòng 5 giây...")
        self.loadingPage.details.show() 
        self.set_loading_state()
        QTimer.singleShot(5000, self.DeleteON)
    def switchToWindowAdd(self):
        self.ser.write(b'a')
        self.loadingPage.details.setText("Vui lòng xác thực vân tay trong vòng 5 giây...")
        self.loadingPage.details.show()
        self.set_loading_state()
        QTimer.singleShot(5000, self.AddON)
        
    def DeleteON(self):
        self.toolbar.show()
        self.login.hide()
        self.details.hide()
        self.add.hide()
        self.delete.show()
        self.loadingPage.hide()
    def AddON(self):
        self.toolbar.show()
        self.login.hide()
        self.details.hide()
        self.add.show()
        self.delete.hide()
        self.loadingPage.hide()
    def DetailsON(self):
        self.toolbar.show()
        self.login.hide()
        self.details.show()
        self.add.hide()
        self.delete.hide()
        self.loadingPage.hide()
        
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
        # self.setCentralWidget(self.loadingPage)
        self.toolbar.hide()
        self.login.hide()
        self.details.hide()
        self.add.hide()
        self.delete.hide()
        self.loadingPage.show()
        self.show()
        
    def processInput(self, key):
        self.queueMain.put(key) 
    def update(self):
        if not self.queueMain.empty():
            self.mainData = self.queueMain.get()
            while True:
                try:
                    if (self.mainData[len(self.mainData)-1] == "0"):
                        self.details.statusDoor.setText("Đóng")
                        self.details.labelDetailIdDoor.setText("ID vân tay đóng cửa: ") 
                    else:
                        self.details.statusDoor.setText("Mở")
                        self.details.labelDetailIdDoor.setText("ID vân tay mở cửa: ")
                        
                    self.details.id.setText(self.mainData[0])
                    break
                except:
                    print("ko co du lieu!")
                    
    def put_id(self, page):
        if page == self.add:
            print('add')
            data = self.add.textDeltailId.text() + '\n'
            self.ser.write(data.encode())
            self.loadingPage.details.setText("Xác nhận vân tay đăng ký 2 lần trước khi chuyển trang sau 10s...")
            self.loadingPage.details.show()
            self.set_loading_state()
            self.ser.write(b'121234\n')
            QTimer.singleShot(14000,self.switchToDetails)
            
        elif page == self.delete:
            print('delete')
            data = self.delete.textDetailIdDelete.text() +'\n'
            self.ser.write(data.encode())
            self.ser.write(b'121234\n')
            QTimer.singleShot(4000,self.switchToDetails)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = SmartDoor()
    sys.exit(app.exec_())