import sys
import os
import inspect # import workaround
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget, plot

### Importing from parent folder workaround
### TODO: Fix this without this workaround
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.getfile)))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import clib.tickers as tickers
import cui.utils as utils

class CrypytoQt(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        try:
            self.setupUI()
        except:
            print('error')

    def setupUI(self) -> None:
        self.setupChart()

    def setupChart(self) -> None:
        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)
        chartData = tickers.fetchChartData('BTC/USD', '1h')
        time = []
        price = []
        for i in chartData:
            time.append(int(utils.convertEpochToDatetime(i[0])))
            price.append(i[1])
        self.graphWidget.plot(time[0:12], price[0:12])