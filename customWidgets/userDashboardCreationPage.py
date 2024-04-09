from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel
from customWidgets import datasetColumnLabel, userDashboard
from statFunctions import mean, variance, median, mode, standardDeviation, statCount, statMin, statMax, ttest
import classes

class userDashboardCreationPage(QWidget):
    def __init__(self, *args, **kwargs):
        super(userDashboardCreationPage, self).__init__(*args, **kwargs)

        self.toolsLayout = QVBoxLayout()
        self.columnLayout = QVBoxLayout()
        self.infoLayout =  QVBoxLayout()

        pageLayout = QHBoxLayout()

        self.userDashboard = userDashboard()
        columnLabel = QLabel("Columns")
        self.columnLayout.addWidget(columnLabel)
        pageLayout.addLayout(self.toolsLayout, 1)
        pageLayout.addLayout(self.columnLayout, 1)
        pageLayout.addWidget(self.userDashboard, 6)    
        pageLayout.addLayout(self.infoLayout, 1)    

        self.setLayout(pageLayout)
        self.createDescriptiveButtons()
        self.createStatTestButtons()
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
    
    def createStatTestButtons(self):
        statTestLayout = QGridLayout()
        titleLabel = QLabel("Statistical tests")

        ttestButton = QPushButton("ttest")
        ttestButton.clicked.connect(lambda: self.userDashboard.addStatLabel("ttest", ttest))

        statTestLayout.addWidget(titleLabel, 0, 0)
        statTestLayout.addWidget(ttestButton, 1, 0)
        self.toolsLayout.addLayout(statTestLayout)
        self.toolsLayout.addStretch()

    def createDescriptiveButtons(self):
        """
        Creates a layout that contains the basic statistical descriptive tools
        """
        
        descriptiveLayout = QGridLayout()

        titleLabel = QLabel("Descriptive Tools")
        meanButton = QPushButton("Mean")
        meanButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Mean", mean))

        medianButton = QPushButton("Median")
        medianButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Median", median))

        modeButton = QPushButton("Mode")
        modeButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Mode", mode))

        standardDeviationButton = QPushButton("Standard deviation")
        standardDeviationButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Standard deviation", standardDeviation))

        VarianceButton = QPushButton("Variance")
        VarianceButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Variance", variance))

        countButton = QPushButton("Count")
        countButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Count", statCount))

        minButton = QPushButton("Minimum")
        minButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Minimum", statMin))

        maxButton = QPushButton("Maximmum")
        maxButton.clicked.connect(lambda: self.userDashboard.addDescriptiveLabel("Maximmum", statMax))

        descriptiveLayout.addWidget(titleLabel, 0, 0)
        descriptiveLayout.addWidget(meanButton, 1, 0)
        descriptiveLayout.addWidget(medianButton, 1, 1)
        descriptiveLayout.addWidget(modeButton, 2, 0)
        descriptiveLayout.addWidget(standardDeviationButton, 2, 1)
        descriptiveLayout.addWidget(VarianceButton, 3, 0)
        descriptiveLayout.addWidget(countButton, 3, 1)
        descriptiveLayout.addWidget(minButton, 4, 0)
        descriptiveLayout.addWidget(maxButton, 4, 1)

        self.toolsLayout.addLayout(descriptiveLayout)
        self.toolsLayout.addStretch()

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

