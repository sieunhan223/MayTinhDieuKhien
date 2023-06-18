import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QToolBar


class WorkerThread(QThread):
    data_processed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            user_input = input("Nhập dữ liệu từ bàn phím: ")
            if user_input == "quit":
                break
            processed_data = user_input.upper()  # Xử lý dữ liệu (Ví dụ: đổi thành chữ hoa)
            self.data_processed.emit(processed_data)


class Content1(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Nhập dữ liệu từ bàn phím:", self)
        self.layout.addWidget(self.label)

        self.worker_thread = WorkerThread()
        self.worker_thread.data_processed.connect(self.update_label)

    def start_processing(self):
        self.worker_thread.start()

    def update_label(self, processed_data):
        self.label.setText("Dữ liệu đã xử lý: " + processed_data)


class Content2(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.button = QPushButton("Lưu và hiển thị", self)
        self.textbox = QLineEdit(self)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.save_and_display)

    def save_and_display(self):
        data = self.textbox.text()
        print("Dữ liệu đã lưu: ", data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ứng dụng Desktop")
        self.resize(400, 200)

        self.toolbar = self.addToolBar('Công cụ')

        self.button1 = self.toolbar.addAction("Mục 1")
        self.button1.triggered.connect(self.show_content1)

        self.button2 = self.toolbar.addAction("Mục 2")
        self.button2.triggered.connect(self.show_content2)

        self.content_widget = QWidget()
        self.setCentralWidget(self.content_widget)

        self.content_layout = QVBoxLayout(self.content_widget)

        self.content1 = Content1()
        self.content_layout.addWidget(self.content1)

        self.content2 = Content2()
        self.content_layout.addWidget(self.content2)

        self.show_content1()

    def show_content1(self):
        self.content1.start_processing()
        self.content1.show()
        self.content2.hide()

    def show_content2(self):
        self.content1.hide()
        self.content2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
