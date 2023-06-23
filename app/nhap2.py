import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QMovie


class ContentWidget(QWidget):
    def __init__(self, content):
        super().__init__()

        self.content_label = QLabel(content)
        self.content_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.content_label)
        self.setLayout(layout)


class LoadingWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.loading_label = QLabel()
        self.loading_movie = QMovie("E:\DaiHoc\Hệ thống máy tính điều khiển\\app\loading.gif")
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()

        layout = QVBoxLayout()
        layout.addWidget(self.loading_label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App Desktop")
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.action1 = QAction("Mục 1", self)
        self.action1.triggered.connect(self.show_content1)
        self.toolbar.addAction(self.action1)

        self.action2 = QAction("Mục 2", self)
        self.action2.triggered.connect(self.show_content2)
        self.toolbar.addAction(self.action2)

        self.content_widget = ContentWidget("Nội dung chính")
        self.setCentralWidget(self.content_widget)

    def show_content1(self):
        self.set_loading_state()
        QTimer.singleShot(2000, lambda: self.update_content_widget(ContentWidget("Nội dung mục 1")))

    def show_content2(self):
        self.set_loading_state()
        QTimer.singleShot(2000, lambda: self.update_content_widget(ContentWidget("Nội dung mục 2")))

    def set_loading_state(self):
        loading_widget = LoadingWidget()
        self.update_content_widget(loading_widget)

    def update_content_widget(self, widget):
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
