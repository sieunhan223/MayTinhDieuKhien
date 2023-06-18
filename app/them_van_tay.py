import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from . import modules

class Add(QWidget):
    def __init__(self): 
        super().__init__()
        self.UIInit()

    def UIInit(self):        
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()

        self.f2 = QFont("Arial", 15)
        self.f2.setBold(True)
        self.labelDeltaiId = QLabel("Nhập ID vân tay mới: ")
        self.labelDeltaiId.setFont(self.f2)
        
        self.textDeltailId = QLineEdit()
        self.textDeltailId.returnPressed.connect(self.put_id)
        self.textDeltailId.setFixedSize(70,30)
        
        self.fbox.addRow(self.labelDeltaiId, self.textDeltailId)

        
        self.but = QPushButton("Gửi", self)
        self.but.move(150,250)
        self.but.setFont(self.f2)
        self.but.setFixedSize(80, 40)
        self.but.clicked.connect(self.put_id)

        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)
        
        self.vbox.addLayout(self.fbox)  # Đặt QVBoxLayout làm layout cho widget trung tâm
        self.setLayout(self.vbox)
        # self.setGeometry(750, 250, 400, 440)
        # self.setWindowTitle("Hệ thống mở cửa thông minh")
        # self.central_widget.setLayout(self.vbox)
        # self.show()
        
    def put_id(self):
        ser = modules.DeviceConnect("COM7", 9600)
        ser.write(b"")
        self.idAdd = self.textDeltailId.text()
        
        print (self.idAdd)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Add()
    my_app.show()
    sys.exit(app.exec_())
