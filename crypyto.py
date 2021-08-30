import sys
import cui.main as cui
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    else:
        print('QApplication instance already exists: %s' % str(app))
    view = cui.CrypytoMainWindow()
    view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()