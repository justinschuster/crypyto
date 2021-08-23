""" Crypyto: Simple application for tracking cryptocurrency prices. """
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout

__version__ = '0.1'
__author__ = 'Justin Schuster'

class CrypytoUI(QMainWindow):
    ''' CrypytoUI's View Class. '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Crypyto')
        self.setFixedSize(235, 235)
        # set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

def main():
    crypyto = QApplication(sys.argv)
    view = CrypytoUI()
    view.show()
    sys.exit(crypyto.exec())

if __name__ == '__main__':
    main()