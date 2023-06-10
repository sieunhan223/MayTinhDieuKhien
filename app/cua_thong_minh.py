
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QVBoxLayout, QMainWindow, QAction
from PyQt5.QtCore import Qt, pyqtSignal, QThread
import login, xoa_van_tay, them_van_tay

class SmartDoor(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.UIinit()
        self.toolbar = self.addToolBar('Công cụ')
        action1 = QAction('Đăng xuất', self)
        action1.triggered.connect(self.switchToWindowLogin)
        self.toolbar.addAction(action1)
        action2 = QAction('Cửa thông minh', self)
        action2.triggered.connect(self.switchToWindowSmartDoor)
        self.toolbar.addAction(action2)
        action3 = QAction('Xóa vân tay', self)
        action3.triggered.connect(self.switchToWindowAdd)
        self.toolbar.addAction(action3)
        action4 = QAction('Tạo vân tay', self)
        action4.triggered.connect(self.switchToWindowDelete)
        self.toolbar.addAction(action4)
    def UIinit(self):
        self.central_widget = QWidget()  # Tạo widget trung tâm
        self.setCentralWidget(self.central_widget)  # Đặt widget trung tâm cho QMainWindow
        
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
        self.central_widget.setLayout(self.vbox)
        self.show()
        
    def switchToWindowLogin(self):
        self.currentWindow = None
        self.login = login.LoginWindow()
        self.close()
        self.login.show()
    def switchToWindowSmartDoor(self):
        self.UIinit()
    def switchToWindowDelete(self):
        self.xoa = them_van_tay.Add()
        self.setCentralWidget(self.xoa)
        self.currentWindow = self.xoa
    def switchToWindowAdd(self):
        self.them = xoa_van_tay.Delete()
        self.setCentralWidget(self.them)
        self.currentWindow = self.them
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = SmartDoor()
    sys.exit(app.exec_())