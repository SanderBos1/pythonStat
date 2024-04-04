from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QLabel
from customWidgets import disiplayCalculationElement, dragLabel
from statFunctions import mean, variance, median, mode, standardDeviation, statCount, statMin, statMax
import classes

class calculateWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(calculateWindow, self).__init__(*args, **kwargs)

        self.toolsLayout = QVBoxLayout()
        self.createdDasboardLayout = QGridLayout()
        self.columnLayout = QVBoxLayout()
        pageLayout = QHBoxLayout()

        pageLayout.addLayout(self.toolsLayout)
        pageLayout.addLayout(self.columnLayout)
        pageLayout.addLayout(self.createdDasboardLayout)    
        pageLayout.addStretch()

        self.setLayout(pageLayout)
        self.createDescriptiveButtons()
        self.showColumns()


    def createDescriptiveButtons(self):
        """
        Creates a layout that contains the basic statistical descriptive tools
        """
        
        descriptiveLayout = QGridLayout()

        titleLabel = QLabel("Descriptive Tools")
        meanButton = QPushButton("Mean")
        meanButton.clicked.connect(lambda: self.addLabel("Mean", mean))

        medianButton = QPushButton("Median")
        medianButton.clicked.connect(lambda: self.addLabel("Median", median))

        modeButton = QPushButton("Mode")
        modeButton.clicked.connect(lambda: self.addLabel("Mode", mode))

        standardDeviationButton = QPushButton("Standard deviation")
        standardDeviationButton.clicked.connect(lambda: self.addLabel("Standard deviation", standardDeviation))

        VarianceButton = QPushButton("Variance")
        VarianceButton.clicked.connect(lambda: self.addLabel("Variance", variance))

        countButton = QPushButton("Count")
        countButton.clicked.connect(lambda: self.addLabel("Count", statCount))

        minButton = QPushButton("Minimum")
        minButton.clicked.connect(lambda: self.addLabel("Minimum", statMin))

        maxButton = QPushButton("Maximmum")
        maxButton.clicked.connect(lambda: self.addLabel("Maximmum", statMax))

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
                    label = dragLabel(str(column))
                    self.columnLayout.addWidget(label)
        self.columnLayout.addStretch()

    def addLabel(self, name, function):

        """
        Adds a label widget to the drawing frame which accept drag events
        On drag events it calculates it associated function on the column it receives.
        
        """
        label = disiplayCalculationElement(name, function)
        self.createdDasboardLayout.addWidget(label)


