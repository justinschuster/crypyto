import sys
import cui.main as cui
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    view = cui.CrypytoMainWindow()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()