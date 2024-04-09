from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QTableView
from models import pandas_dataset
import classes


class viewDatasetWidget(QWidget):
    def __init__(self, parent=None):
        super(viewDatasetWidget, self).__init__(parent)

        self.dataTable = QTableView()
        menuLayout = QVBoxLayout()

        tableLayout =  QHBoxLayout()
        tableLayout.addWidget(self.dataTable)


        pageLayout =  QHBoxLayout()
        pageLayout.addLayout(menuLayout)
        pageLayout.addLayout(tableLayout)
        self.setLayout(pageLayout)
        self.loadDataset()
        
    def loadDataset(self):
        self.dataTable.setAlternatingRowColors(True)
        self.model = pandas_dataset(classes.selectedDataset)   

        self.dataTable.setModel(self.model)

