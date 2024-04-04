from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QTabWidget, QMainWindow, QMenuBar, QTextEdit
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import pandas as pd
import pickle
from windows import calculateWindow, tableWindow
import sys
import os
from customWidgets import CustomTitleBar
import classes
from classes import userDataset


#declares the global dataset variable


# Subclass QMainWindow to customize your application's main window
class stat_app(QMainWindow):
    def __init__(self):
        super().__init__()



        self.textEdit = QTextEdit()
        
        self.setWindowTitle("Stat program")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.titleBar = CustomTitleBar(self)
        mainApp = QWidget()
        mainAppLayout = QVBoxLayout()


        # Defines layout where widgets on main page are placed
        self.mainFrame = QVBoxLayout()

        mainAppLayout.addWidget(self.titleBar)
        mainAppLayout.addLayout(self.mainFrame)
        mainAppLayout.addStretch()
        mainApp.setLayout(mainAppLayout)

        self.setCentralWidget(mainApp)
        self.setGeometry(100, 100, 600, 400) 
        self.showMaximized() 


        #sets the widgets in the window

        self.create_menu()


        
    def calculateTab(self):
        "Sets the GUI of the Home page"
        self.fundament = calculateWindow()
        return self.fundament


    def showTableTab(self):
        "Sets the GUI of the page that displays the loaded dataset"
        self.newTabelWindow = tableWindow(self)
        self.newTabelWindow.setWindowTitle("UIWindow")
        if classes.selectedDataset is not None:
            self.newTabelWindow.loadDataset(classes.selectedDataset)
        return self.newTabelWindow
    
    def createTabs(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.addTab(self.calculateTab(), "calculate")
        self.tabs.addTab(self.showTableTab(), "dataset")
        self.mainFrame.addWidget(self.tabs)


    def create_menu(self):
        """
        Creates the main menu of the program
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
        Loads your process
        """
        fileName = QFileDialog.getOpenFileName(self, 'Opened file')
        if fileName[0] == "":
            print("no name was selected")
        else:
            with open(fileName[0] , 'rb') as f:
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
        """
        fileName = QFileDialog.getSaveFileName(self, 'Save File')
        if fileName[0] == "":
            print("no name was selected")
        else:
            createdWidgets = self.fundament.getState()
            saveState = {
                "dataset" : classes.selectedDataset,
                "createdWidgets" : createdWidgets
            }
            saveFile = open(f"{fileName[0]}", 'wb')
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

    with open('styles/styles.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)

    my_app = stat_app()
    my_app.show()
    sys.exit(app.exec())
