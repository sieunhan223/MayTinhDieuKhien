import sys
import queue
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

class KeyboardThread(QThread):
    key_pressed = pyqtSignal(str)
    
    def run(self):
        while True:
            key = sys.stdin.readline().strip()
            self.key_pressed.emit(key)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ứng dụng Desktop với PyQt5")
        
        self.label = QLabel("Nhập thông tin từ bàn phím", self)
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.keyboard_queue = queue.Queue()
        
        self.keyboard_thread = KeyboardThread()
        self.keyboard_thread.key_pressed.connect(self.process_key)
        self.keyboard_thread.start()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)  # Cập nhật label sau mỗi 1 giây
        
    def process_key(self, key):
        self.keyboard_queue.put(key)
        
    def update_label(self):
        if not self.keyboard_queue.empty():
            text = self.keyboard_queue.get()
            self.label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
