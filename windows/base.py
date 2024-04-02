from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QTableView



class base(QWidget):
    def __init__(self, parent=None):
        super(base, self).__init__(parent)
        self.CPSBTN = QPushButton("showDataset", self)
        self.CPSBTN.move(100, 350)

        menuLayout = QVBoxLayout()
        menuLayout.addWidget(self.CPSBTN)

        pageLayout =  QHBoxLayout()
        pageLayout.addLayout(menuLayout)

        self.setLayout(pageLayout)

class tableWindow(QWidget):
    def __init__(self, parent=None):
        super(tableWindow, self).__init__(parent)

        # Button to go back to calculation screen
        self.ToolsBTN = QPushButton('calculate', self)
        self.dataTable = QTableView()

        menuLayout = QVBoxLayout()
        menuLayout.addWidget(self.ToolsBTN)

        tableLayout =  QHBoxLayout()
        tableLayout.addWidget(self.dataTable)


        pageLayout =  QHBoxLayout()
        pageLayout.addLayout(menuLayout)
        pageLayout.addLayout(tableLayout)
        self.setLayout(pageLayout)
        
