''' View elements.
    TODO: Change file name
'''

from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

data = [
    ['BTC', '58000', '10'],
    ['ETH', '30000', '7.41'],
    ['ADA', '2.78', '14']
]

class CrypytoUI(QWidget):
    ''' CrypytoUI's View Class. '''
    def __init__(self):
        ''' Initialize window. '''
        super().__init__()

        self.setWindowTitle('Crypyto')
        self.setFixedSize(750, 750)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def createTable(self):
        ''' Method to create the table. '''
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Price', '24hr G/L %'])
        for i in range(len(data)):
            item_name = QTableWidgetItem(data[i][0])
            item_price = QTableWidgetItem(data[i][1])
            item_gl = QTableWidgetItem(data[i][2])
            self.tableWidget.setItem(i, 0, item_name)
            self.tableWidget.setItem(i, 1, item_price)
            self.tableWidget.setItem(i, 2, item_gl) 

