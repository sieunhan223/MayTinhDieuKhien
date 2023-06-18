
import sys, queue
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QVBoxLayout
from PyQt5.QtCore import  Qt, pyqtSignal, QThread, QTimer
from . import modules
class DeltaisThread(QThread):
    def __init__(self, ser) -> None:
        super().__init__()
        self.ser = ser
    input = pyqtSignal(str)
    
    def run(self):
        while True:
            key = self.ser.readline().decode().strip()
            self.input.emit(key)
    

class Details(QWidget):
    def __init__(self, ser) -> None:
        super().__init__()
        self.vbox = QVBoxLayout()
        self.fbox = QFormLayout()
        self.ser = ser
        self.UIinit()

    def UIinit(self):
        self.queueMain = queue.Queue()
        #Tạo font
        self.f2 = QFont("Arial", 15)
        self.f2.setBold(True)
        #Trạng thái cửa
        self.labelStatusDoor = QLabel(text="Trạng thái cửa: ")
        self.labelStatusDoor.setFont(self.f2)
        self.statusDoor = QLabel()
        self.statusDoor.setFixedSize(80,40)
        self.statusDoor.setStyleSheet("color :red")
        self.statusDoor.setFont(self.f2)
        self.fbox.addRow(self.labelStatusDoor,self.statusDoor)
        #ID
        self.labelDetailIdDoor = QLabel(f"ID vân tay {self.statusDoor.text().lower()} cửa: ")
        self.labelDetailIdDoor.setFont(self.f2)
        self.id = QLabel()
        self.id.setFixedSize(80,40)
        self.id.setFont(self.f2)
        self.fbox.addRow(self.labelDetailIdDoor,self.id)
        #Thực hiện xử lý hiển thị
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.threadInput = DeltaisThread(self.ser)
        self.threadInput.input.connect(self.processInput)
        self.threadInput.start()
        
        
        self.fbox.setFormAlignment(Qt.AlignHCenter)
        self.fbox.setFormAlignment(Qt.AlignVCenter)
        
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.fbox)
        
    def processInput(self, key):
        self.queueMain.put(key) 
    def update(self):
        if not self.queueMain.empty():
            data = self.queueMain.get()
            self.statusDoor.setText("Đóng" if (data[1] == "0") else "Mở")
            self.id.setText(data[0])
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_app = Details()
    my_app.show()
    sys.exit(app.exec_())