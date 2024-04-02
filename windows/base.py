from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QTableView



class base(QWidget):
    def __init__(self, parent=None):
        super(base, self).__init__(parent)


        pageLayout = QVBoxLayout()

        self.setLayout(pageLayout)

class tableWindow(QWidget):
    def __init__(self, parent=None):
        super(tableWindow, self).__init__(parent)

        self.dataTable = QTableView()

        menuLayout = QVBoxLayout()

        tableLayout =  QHBoxLayout()
        tableLayout.addWidget(self.dataTable)


        pageLayout =  QHBoxLayout()
        pageLayout.addLayout(menuLayout)
        pageLayout.addLayout(tableLayout)
        self.setLayout(pageLayout)
        
