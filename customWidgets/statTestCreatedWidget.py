from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel
from statFunctions import ttest
class statTestCreatedWidget(QWidget):
    """
    Creates a widget that contains the following elements:

    functionLabel: A label that displays which function is calculated when a label is dropped into this widget.
    DeleteButton: When pressed, removes the widget from the window.
    columnLabel: Displays one of the columns  of the dataset on which column the function is calculated.
    columnLabel2: Displays one of the columns  of the dataset on which column the function is calculated.
    answerLabel: Displays the answer of the calculation.

    Accepts drag events.
    """
    def __init__(self, position, column = "No column Selected", column2 = "No column Selected", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.column = column
        self.column2 = column2
        self.position = position

        self.widgetLayout = QVBoxLayout()
        
        self.informationLayout = QHBoxLayout()

        self.interactionLayout = QHBoxLayout()
        self.interactionLayout.addStretch(1)

        deleteButton = QPushButton()
        deleteButton.setText("X")      
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.column )

        self.columnLabel2 = chosenColumnLabel(self.calculateFunction)
        self.columnLabel2.setText(self.column2)
        
        pvalueLayout = QVBoxLayout()
        pvalueLabel = QLabel("p value")
        self.pvalueanswerLabel = QLabel()
        pvalueLayout.addWidget(pvalueLabel)
        pvalueLayout.addWidget(self.pvalueanswerLabel)

        self.informationLayout.addWidget(self.columnLabel)
        self.informationLayout.addWidget(self.columnLabel2)
        self.informationLayout.addLayout(pvalueLayout)
        self.interactionLayout.addWidget(deleteButton)

        self.widgetLayout.addLayout(self.interactionLayout)
        self.widgetLayout.addLayout(self.informationLayout)

        self.setLayout(self.widgetLayout)
    
        if self.columnLabel.getText() != "No column Selected" and self.columnLabel2.getText() != "No column Selected" :
            self.calculateFunction()

        self.setMaximumHeight(200)

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getData(self):
        """ 
        Returns all information needed to recreate the object
        """
        return {
            "column":self.columnLabel.getText(), 
            "column2": self.columnLabel2.getText(),
            "position": self.position,
            "type": "statTest"
        }
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()

    def calculateFunction(self):
        """
        When a column is dropped into the widget it executes this function.
        First it checks if it has two chosen columns
        Than it calculates the ttest p value and sets a label with the answer
        """
        if self.columnLabel.getText() != "No column Selected" and self.columnLabel2.getText() != "No column Selected" :
            answer = ttest(self.columnLabel.getText(), self.columnLabel2.getText())
            self.pvalueanswerLabel.setText(str(answer))


    #Defines what happens when the widget is dragged
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())


            drag.exec(Qt.DropAction.MoveAction)
    
    

