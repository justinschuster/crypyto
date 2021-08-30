from pyqtgraph import PlotWidget
from PyQt5.QtWidgets import QDockWidget, QListWidget

import clib.tickers as tickers
from cui.items import DateAxisItem

def createPlotWidget(): 
    """ Setup main plot. """
    plotWidget = PlotWidget()
    axis = DateAxisItem(orientation='bottom')
    axis.attachToPlotItem(plotWidget.getPlotItem())
    time_data, price_data = tickers.fetchChartData('BTC/USD', '1m')
    plotWidget.plot(x=time_data, y=price_data)
    plotWidget.getPlotItem().setTitle('BTC/USD')
    plotWidget.getPlotItem().showGrid(x=True, y=True, alpha=0.2)     
    return plotWidget

def createTaskBar():
    """ Setup task bar. """
    pass

def createWatchList(mainWindow): 
    """ Setup watch list. """
    watch = QDockWidget("Watch List", mainWindow)
    listWidget = QListWidget()
    listWidget.addItem('item1')
    listWidget.addItem('item2')
    watch.setWidget(listWidget)
    watch.setFloating(False) 
    return watch