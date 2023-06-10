import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFormLayout, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt

class Add(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.UIInit()

    def UIInit(self):
        self.central_widget = QWidget()  # Tạo widget trung tâm
        self.setCentralWidget(self.central_widget)  # Đặt widget trung tâm cho QMainWindow
        
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()

        self.f1 = QFont("Arial", 15)
        self.f1.setBold(True)
        self.l1 = QLabel("Nhập ID vân tay mới: ")
        self.l1.setFont(self.f1)
        
        self.text = QLineEdit()
        self.text.returnPressed.connect(self.get_id)
        self.text.setFixedSize(70,30)
        
        self.fbox.addRow(self.l1, self.text)

        
        self.but = QPushButton("Gửi", self)
        self.but.move(150,250)
        self.but.setFont(self.f1)
        self.but.setFixedSize(80, 40)
        self.but.clicked.connect(self.get_id)

        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)
        
        self.vbox.addLayout(self.fbox)  # Đặt QVBoxLayout làm layout cho widget trung tâm
        
        self.setGeometry(750, 250, 400, 440)
        self.setWindowTitle("Hệ thống mở cửa thông minh")
        self.central_widget.setLayout(self.vbox)
        self.show()
        
    def get_id(self):
        self.input_id = self.text.text()
        print (self.input_id)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Add()
    sys.exit(app.exec_())
