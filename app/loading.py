import sys
import typing
from PyQt5.QtCore import  Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout


class LoadingWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.details = QLabel()
        self.details.setStyleSheet("color :red")
        self.loading_label = QLabel()
        self.loading_movie = QMovie("E:\DaiHoc\Hệ thống máy tính điều khiển\\app\loading.gif")
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.loading_label)
        mainLayout.addWidget(self.details)
        
        self.setLayout(mainLayout)
        mainLayout.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = LoadingWidget()
    window.show()

    sys.exit(app.exec_())
