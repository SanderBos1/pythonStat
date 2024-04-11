from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel
from statFunctions import mean, variance, median, mode, standardDeviation, statCount, statMin, statMax

class descriptiveWidget(QWidget):
    """
    Creates a widget that displays the discriptive information of one column
    Accepts drag events.
    """
    def __init__(self, position, column= "No column selected", parent=None):
        super(descriptiveWidget, self).__init__(parent)

        self.column = column
        self.position = position
        self.type = "descriptive"


        self.widgetLayout = QVBoxLayout()
        self.informationLayout = QHBoxLayout()

        self.interactionLayout = QHBoxLayout()
        self.interactionLayout.addStretch(1)

        # defines all logic to display the mean
        meanLayout = QVBoxLayout()
        meanLabel = QLabel("mean")
        self.meanAnswerLabel = QLabel()
        meanLayout.addWidget(meanLabel)
        meanLayout.addWidget(self.meanAnswerLabel)

        # defines all logic to display the median

        medianLayout = QVBoxLayout()
        medianLabel = QLabel("median")
        self.medianAnswerLabel = QLabel()
        medianLayout.addWidget(medianLabel)
        medianLayout.addWidget(self.medianAnswerLabel)

        # defines all logic to display the mode

        modeLayout = QVBoxLayout()
        modeLabel = QLabel("mode")
        self.modeAnswerLabel = QLabel()
        modeLayout.addWidget(modeLabel)
        modeLayout.addWidget(self.modeAnswerLabel)

        # defines all logic to display the variance
        varianceLayout = QVBoxLayout()
        varianceLabel = QLabel("variance")
        self.varianceAnswerLabel = QLabel()
        varianceLayout.addWidget(varianceLabel)
        varianceLayout.addWidget(self.varianceAnswerLabel)

        # defines all logic to display the standard deviation
        sdLayout = QVBoxLayout()
        sdLabel = QLabel("standard deviation")
        self.sdAnswerLabel = QLabel()
        sdLayout.addWidget(sdLabel)
        sdLayout.addWidget(self.sdAnswerLabel)

        # defines all logic to display the minimum
        minLayout = QVBoxLayout()
        minLabel = QLabel("Min")
        self.minAnswerLabel = QLabel()
        minLayout.addWidget(minLabel)
        minLayout.addWidget(self.minAnswerLabel)

        # defines all logic to display the maximum
        maxLayout = QVBoxLayout()
        maxLabel = QLabel("Max")
        self.maxAnswerLabel = QLabel()
        maxLayout.addWidget(maxLabel)
        maxLayout.addWidget(self.maxAnswerLabel)

        # defines all logic to display the Count
        countLayout = QVBoxLayout()
        countLabel = QLabel("Count")
        self.countAnswerLabel = QLabel()
        countLayout.addWidget(countLabel)
        countLayout.addWidget(self.countAnswerLabel)

        deleteButton = QPushButton()
        deleteButton.setText("X")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.column)
        

        self.informationLayout.addWidget(self.columnLabel)
        self.informationLayout.addLayout(meanLayout)
        self.informationLayout.addLayout(medianLayout)
        self.informationLayout.addLayout(modeLayout)
        self.informationLayout.addLayout(varianceLayout)
        self.informationLayout.addLayout(sdLayout)
        self.informationLayout.addLayout(minLayout)
        self.informationLayout.addLayout(maxLayout)
        self.informationLayout.addLayout(countLayout)


        self.interactionLayout.addWidget(deleteButton)

        self.widgetLayout.addLayout(self.interactionLayout)
        self.widgetLayout.addLayout(self.informationLayout)

        self.setLayout(self.widgetLayout)

        #layout
        self.setMaximumHeight(200)
        if self.column != "No column selected":
            self.calculateFunction()

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getData(self):
        """ 
        Returns all information needed to recreate a descriptiveWidget
        Returns:
            A dictionary containing:
                Column: The dataset column that is associated with it
                Type: A string so that the program can read which widget has to be created.
                Position: The position of the widget

        """
        return {
            "column":self.column, 
            "type": self.type,
            "position": self.position
        }
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()


    def calculateFunction(self):
        """
        Calculates all descriptive functions using the selected column and sets the labels accordingly
        """

        self.column = self.columnLabel.getText()
        meanAnswer = mean(self.column )
        self.meanAnswerLabel.setText(str(meanAnswer))

        medianAnswer = median(self.column )
        self.medianAnswerLabel.setText(str(medianAnswer))

        modeAnswer = mode(self.column )
        self.modeAnswerLabel.setText(str(modeAnswer))

        varianceAnswer = variance(self.column )
        self.varianceAnswerLabel.setText(str(varianceAnswer))

        sdAnswer = standardDeviation(self.column)
        self.sdAnswerLabel.setText(str(sdAnswer))

        minAnswer = statMin(self.column)
        self.minAnswerLabel.setText(str(minAnswer))

        maxAnswer = statMax(self.column)
        self.maxAnswerLabel.setText(str(maxAnswer))

        countAnswer = statCount(self.column)
        self.countAnswerLabel.setText(str(countAnswer))
    #Defines what happens when the widget is dragged

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())


            drag.exec(Qt.DropAction.MoveAction)
