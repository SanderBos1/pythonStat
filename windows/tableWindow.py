from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QTableView
from models import pandas_dataset


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
        
    def loadDataset(self, df):
        self.dataTable.setAlternatingRowColors(True)
        self.model = pandas_dataset(df)   

        self.dataTable.setModel(self.model)

