from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel
from customWidgets import datasetColumnLabel, userCanvas
from PyQt6.QtCore import Qt

import classes

class canvasCreationPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(canvasCreationPage, self).__init__(*args, **kwargs)

        self.toolsLayout = QGridLayout()
        self.toolsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.columnLayout = QVBoxLayout()

        pageLayout = QHBoxLayout()

        self.userDashboard = userCanvas()
        columnLabel = QLabel("Columns")
        self.columnLayout.addWidget(columnLabel)
        pageLayout.addLayout(self.toolsLayout, 1)
        pageLayout.addLayout(self.columnLayout, 1)
        pageLayout.addWidget(self.userDashboard, 6)    

        self.setLayout(pageLayout)
        self.createButtons()
        self.showColumns()

    def getState(self):
        """
        Returns a list that corresponds to all the widgets that a user has created and their state data
        This list is used to save the user state
        """
        return self.userDashboard.getState()
    
    def setState(self, savedState):
        """
        Creates a state from a list of dictionaries that corresponds to the previous created widgets
        """
        return self.userDashboard.setState(savedState)
    

    def createButtons(self):
        """
        Creates a layout that contains the basic statistical descriptive tools
        """
        

        titleLabel = QLabel("Descriptive Tools")
        descriptiveButton = QPushButton("descriptive Overview")
        descriptiveButton.clicked.connect(lambda: self.userDashboard.addDescriptiveWidget())

        ttestButton = QPushButton("Ttest")
        ttestButton.clicked.connect(lambda: self.userDashboard.addStatLabel())

        self.toolsLayout.addWidget(titleLabel, 0, 0)
        self.toolsLayout.addWidget(descriptiveButton, 1, 0)
        self.toolsLayout.addWidget(ttestButton, 1, 1)
  


    def showColumns(self):
        """
        Displays the columns of the global dataset as labels, which are dragable

        """
        if classes.selectedDataset is not None:
            columns = classes.selectedDataset.getColumns()
            for column in columns:
                    label = datasetColumnLabel(str(column))
                    self.columnLayout.addWidget(label)
        self.columnLayout.addStretch()

