from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QTabWidget, QMainWindow
from PyQt6.QtGui import QAction
import pandas as pd
from windows import calculateWindow, tableWindow
import sys
import os

# Subclass QMainWindow to customize your application's main window
class stat_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file = None
        self.df = None
        self.setWindowTitle("Statistical calculator")
        self.setGeometry(100, 100, 600, 400) 
        self.showMaximized() 

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

    def calculateTab(self):
        "Sets the GUI of the Home page"
        self.fundament = calculateWindow(self)
        return self.fundament


    def showTableTab(self):
        "Sets the GUI of the page that displays the loaded dataset"
        self.newTabelWindow = tableWindow(self)
        self.newTabelWindow.setWindowTitle("UIWindow")
        if self.df is not None:
            self.newTabelWindow.loadDataset(self.df)
        return self.newTabelWindow



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

        self.newTabelWindow.loadDataset(self.df)
        self.fundament.updatedf(self.df)
        self.fundament.toolbox()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = stat_app()
    my_app.show()
    sys.exit(app.exec())
