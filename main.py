from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QTabWidget, QMainWindow
from PyQt6.QtGui import QAction
import pandas as pd
from models import pandas_dataset
from windows import base, tableWindow
import sys
import os

# Subclass QMainWindow to customize your application's main window
class stat_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file = None
        self.df = None
        self.setWindowTitle("Statistical calculator")
        self.window_width, self.window_height = 700, 900
        self.resize(self.window_width, self.window_height)

        #sets the widgets in the window
        self.mainFrame = QWidget()
        self.layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.addTab(self.calculateTab(), "calculate")
        tabs.addTab(self.showTableTab(), "dataset")
        self.layout.addWidget(tabs)
        self.mainFrame.setLayout(self.layout)

        
        self.setCentralWidget(self.mainFrame)
        self.create_menu()
        self.calculateTab()

    def calculateTab(self):
        "Sets the GUI of the Home page"
        fundament = base()
        return fundament


    def showTableTab(self):
        "Sets the GUI of the page that displays the loaded dataset"
        self.newTabelWindow = tableWindow(self)
        self.newTabelWindow.setWindowTitle("UIWindow")
        if self.df is not None:
            self.loadDataset()
        return self.newTabelWindow

    def loadDataset(self):
        self.newTabelWindow.dataTable.resize(800, 500)
        self.newTabelWindow.dataTable.horizontalHeader().setStretchLastSection(True)
        self.newTabelWindow.dataTable.setAlternatingRowColors(True)
        self.model = pandas_dataset(self.df)   

        self.newTabelWindow.dataTable.setModel(self.model)

        self.show()

    def create_menu(self):
        menu = self.menuBar()
        load_file_action = QAction("&load file", self)
        load_file_action.triggered.connect(self.getfile)



        file_menu = menu.addMenu("&File")
        file_menu.addAction(load_file_action)


    def getfile(self):
        """Loads a csv file to a dataframe and loads the data into the dataTable page """
        file_filter = 'Data File (*.xlsx *.csv *.dat)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        df = pd.read_csv(response[0])
        self.df = df
        self.loadDataset()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = stat_app()
    my_app.show()
    sys.exit(app.exec())
