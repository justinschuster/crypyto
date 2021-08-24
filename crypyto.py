import sys
from PyQt5.QtWidgets import QApplication
from cui.main import CrypytoQt

def main():
    app = QApplication(sys.argv)
    view = CrypytoQt()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()