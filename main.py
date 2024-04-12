from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QTabWidget, QMainWindow, QMenuBar
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import pandas as pd
import pickle
import sys
import os
from customWidgets import CustomTitleBar, canvasCreationPage, viewDatasetWidget
import classes
from classes import userDataset




class stat_app(QMainWindow):
    """
    Creates the main application window.
    """
    def __init__(self):
        super().__init__()
        
        self.extension = ".pyStat"

        self.setWindowTitle("Stat program")

        # makes the window frameless


        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.titleBar = CustomTitleBar(self)
        mainApp = QWidget()
        mainAppLayout = QVBoxLayout()


        # Defines layout where widgets on main page are placed
        self.mainFrame = QVBoxLayout()

        mainAppLayout.addWidget(self.titleBar)
        mainAppLayout.addLayout(self.mainFrame)
        mainApp.setLayout(mainAppLayout)

        self.setCentralWidget(mainApp)
        self.showMaximized() 


        #Creates the window menu of the page
        self.create_menu()


        
    def calculateTab(self):
        """
        Creates the tab where the widgets that user create are placed.
        """
        self.fundament = canvasCreationPage()
        return self.fundament


    def showTableTab(self):
        """
        Sets the tab that displays the dataset

        """

        self.newTabelWindow = viewDatasetWidget(self)
        self.newTabelWindow.setWindowTitle("UIWindow")
        return self.newTabelWindow
    
    def createTabs(self):
        """
        Creates a tap widget and creates two tap
        The first tab displays the dashboard creation tap
        The second tab displays the dataset view page
        """
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.addTab(self.calculateTab(), "calculate")
        self.tabs.addTab(self.showTableTab(), "dataset")
        self.mainFrame.addWidget(self.tabs)


    def create_menu(self):
        """
        Creates the main menu of the program and adds it to the mainFrame.
        """
        menu = QMenuBar(self)
        
        load_csv_action = QAction("&Import csv", self)
        load_csv_action.setShortcut("Ctrl+L")
        load_csv_action.triggered.connect(self.getCSV)

        save_file_action = QAction("Save", self)
        save_file_action.setShortcut("Ctrl+S")
        save_file_action.triggered.connect(self.saveFile)

        load_file_action = QAction("Load", self)
        load_file_action.setShortcut("Ctrl+O")
        load_file_action.triggered.connect(self.loadFile)


        file_menu = menu.addMenu("&File")

        file_menu.addAction(save_file_action)
        file_menu.addAction(load_file_action)
        file_menu.addAction(load_csv_action)

        self.mainFrame.addWidget(menu)

    def loadFile(self):
        """
        Loads a save file of the pythonstat app
        """
        fileName, _ = QFileDialog.getOpenFileName(self, filter="pyStat Files (*" + self.extension + ");;")
        if fileName == "":
            print("no name was selected")
        else:
            with open(fileName , 'rb') as f:
                savedState = pickle.load(f)
            classes.selectedDataset = savedState['dataset']

            if hasattr(self, 'tabs'):
                self.mainFrame.removeWidget(self.tabs)
                self.tabs.deleteLater()
                self.tabs = None
            self.createTabs()
        self.fundament.setState(savedState['createdWidgets'])

    def saveFile(self):
        """
        Saves your process
        @extension: determines the extension of the file
        """
        fileName, _ = QFileDialog.getSaveFileName(self,  filter="pyStat Files (*" + self.extension + ");;")
        if fileName == "":
            print("no name was selected")
        else:
            if not fileName.endswith(self.extension):
                fileName += self.extension
            createdWidgets = self.fundament.getState()
            saveState = {
                "dataset" : classes.selectedDataset,
                "createdWidgets" : createdWidgets
            }
            saveFile = open(f"{fileName}", 'wb')
            pickle.dump(saveState, saveFile)
            saveFile.close()

    def getCSV(self):
        """
        Loads a csv to the global variable selectDataset
        Recreates the tabs so that they display all elements that need a dataset to be loaded
        
        """
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
        )
        if response[0] == "":
            print("no file was selected")
        else:
            df = pd.read_csv(response[0])
            classes.selectedDataset = userDataset(df)
            if hasattr(self, 'tabs'):
                self.mainFrame.removeWidget(self.tabs)
                self.tabs.deleteLater()
                self.tabs = None
            self.createTabs()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("styles/styles.qss").read())

    my_app = stat_app()
    my_app.show()
    sys.exit(app.exec())
