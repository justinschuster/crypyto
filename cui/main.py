import sys

from PyQt5.QtWidgets import QLabel, QMainWindow
from pyqtgraph import PlotWidget, AxisItem
import pyqtgraph as pg

# Temporary
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import clib.tickers as tickers
import cui.widgets as widgets
from cui.items import DateAxisItem
           
class CrypytoMainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'Crypyto'
        self.width = 1200
        self.height = 900
        self.left = 0
        self.top = 500

        try:
            self.setupUI()
        except Exception as e:
            print('Failed to create MainWindow:', str(e)) 
            sys.exit(-1)

    def setupUI(self) -> None:
        self.setupChart()

    def setupChart(self) -> None:
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QHBoxLayout()  

        # Taskbar
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction('About')
        file.addAction('Quit')

        # Chart 
        self.plotWidget = widgets.createPlotWidget()
        layout.addWidget(self.plotWidget)

        # Watch List
        self.items = QDockWidget("Watch List", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)

        self.setCentralWidget(self.plotWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)