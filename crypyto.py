import sys
from cui.main import CrypytoQt
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    view = CrypytoQt()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()