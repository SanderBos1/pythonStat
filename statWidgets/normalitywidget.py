from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel
from statFunctions import normalTest

class normalityWidget(QWidget):
    """
    Creates a widget that displays the discriptive information of one column
    Accepts drag events.
    """
    def __init__(self, position, column= "No column selected", parent=None):
        super(normalityWidget, self).__init__(parent)

        self.column = column
        self.position = position
        self.type = "normal"


        self.widgetLayout = QVBoxLayout()
        self.informationLayout = QHBoxLayout()

        self.interactionLayout = QHBoxLayout()
        self.interactionLayout.addStretch(1)

        # defines all logic to display the pvalue of the normal test
        pvalueLayout = QVBoxLayout()
        pvalueLabel = QLabel("p value")
        self.pvalueanswerLabel = QLabel()
        pvalueLayout.addWidget(pvalueLabel)
        pvalueLayout.addWidget(self.pvalueanswerLabel)

        functionlabel = QLabel("Normal Test")

        deleteButton = QPushButton()
        deleteButton.setText("X")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.column)
        

        self.informationLayout.addWidget(self.columnLabel)
        self.informationLayout.addLayout(pvalueLayout)

        self.interactionLayout.addWidget(functionlabel)
        self.interactionLayout.addWidget(deleteButton)

        self.widgetLayout.addLayout(self.interactionLayout)
        self.widgetLayout.addLayout(self.informationLayout)

        self.setLayout(self.widgetLayout)

        #layout
        self.setMaximumHeight(250)
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
        answer = normalTest(self.column)
        if not isinstance(answer, str):
            self.pvalueanswerLabel.setText(str(answer['pValue']))
        else:
            self.pvalueanswerLabel.setText(answer)

    #Defines what happens when the widget is dragged

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())


            drag.exec(Qt.DropAction.MoveAction)
