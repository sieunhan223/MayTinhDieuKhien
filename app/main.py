import login
import sys

if __name__ == "__main__" :
    app = login.QApplication(sys.argv)
    my_app = login.LoginWindow()
    sys.exit(app.exec_())