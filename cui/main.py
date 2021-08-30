import sys

from PyQt5.QtWidgets import QLabel, QMainWindow
from pyqtgraph import PlotWidget, AxisItem
import pyqtgraph as pg

# Temporary
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import clib.tickers as tickers
from cui.items import DateAxisItem
           
class CrypytoMainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        try:
            self.setupLayout()
            self.setupUI()
        except Exception as e:
            print('Failed to create MainWindow:', str(e)) 
            sys.exit(-1)

    def setupLayout(self):
        #self.grid = QGridLayout()
        #self.setLayout(self.grid)
        pass

    def setupUI(self) -> None:
        self.setupChart()

    def setupChart(self) -> None:
        self.plotWidget = PlotWidget()
        self.setCentralWidget(self.plotWidget)
        
        axis = DateAxisItem(orientation='bottom')
        axis.attachToPlotItem(self.plotWidget.getPlotItem())

        self.time_data, self.price_data = tickers.fetchChartData('BTC/USD', '1m')
        self.plotWidget.plot(x=self.time_data, y=self.price_data)
        self.plotWidget.getPlotItem().setTitle('BTC/USD')
        self.plotWidget.getPlotItem().showGrid(x=True, y=True, alpha=0.2)  