""" Crypyto: Simple application for tracking cryptocurrency prices. """
import sys

from PyQt5.QtWidgets import QApplication

from view.mainview import CrypytoUI

__version__ = '0.1'
__author__ = 'Justin Schuster'

def main():
    crypyto = QApplication(sys.argv)
    view = CrypytoUI()
    view.show()
    sys.exit(crypyto.exec())

if __name__ == '__main__':
    main()