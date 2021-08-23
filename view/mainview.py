''' View elements.
    TODO: Change file name
'''

from PyQt5.QtWidgets import QMainWindow, QWidget

class CrypytoUI(QMainWindow):
    ''' CrypytoUI's View Class. '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Crypyto')
        self.setFixedSize(235, 235)
        # set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)