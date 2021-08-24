import sys
import os
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget, plot

time = [1, 2, 3, 4, 5]
price = [10, 25, 8, 19, 30]

class CrypytoQt(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        try:
            self.setupUI()
        except:
            print('Error. Closing program...')
            sys.exit(1)

    def setupUI(self) -> None:
        self.setupChart()

    def setupChart(self) -> None:
        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.plot(time, price)