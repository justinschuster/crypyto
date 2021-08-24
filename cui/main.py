from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget, plot

import clib.tickers as tickers
import cui.utils as utils

class CrypytoQt(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        try:
            self.setupUI()
        except Exception as e:
            print('error')
            print(type(e))

    def setupUI(self) -> None:
        self.setupChart()

    def setupChart(self) -> None:
        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)
        chartData = tickers.fetchChartData('BTC/USD', '1h')
        time = []
        price = []
        for i in chartData:
            time.append(utils.convertEpochToDatetime(i[0]))
            price.append(i[1])
        self.graphWidget.plot(time, price)