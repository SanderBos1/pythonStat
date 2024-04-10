from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel

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
    def __init__(self, name, function, position, column = "No column Selected", column2 = "No column Selected", answer= "",  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.function = function
        self.column = column
        self.column2 = column2
        self.answer = answer
        self.position = position

        self.widgetLayout = QVBoxLayout()
        
        self.informationLayout = QHBoxLayout()

        self.interactionLayout = QHBoxLayout()
        self.interactionLayout.addStretch(1)

        self.functionLabel = QLabel()
        self.functionLabel.setText(self.name)

        deleteButton = QPushButton()
        deleteButton.setText("X")      
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.column )

        self.columnLabel2 = chosenColumnLabel(self.calculateFunction)
        self.columnLabel2.setText(self.column2)
        
        self.answerLabel = QLabel()
        self.answerLabel.setText(answer)

        self.informationLayout.addWidget(self.functionLabel)
        self.informationLayout.addWidget(self.columnLabel)
        self.informationLayout.addWidget(self.columnLabel2)
        self.informationLayout.addWidget(self.answerLabel)
        self.interactionLayout.addWidget(deleteButton)

        self.widgetLayout.addLayout(self.interactionLayout)
        self.widgetLayout.addLayout(self.informationLayout)

        self.setLayout(self.widgetLayout)

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position

    def getData(self):
        """ 
        Returns all information needed to recreate the object
        """
        return {
            "text": self.name,
            "function":self.function, 
            "column":self.columnLabel.getText(), 
            "column2": self.columnLabel2.getText(),
            "answer": self.answer,
            "position": self.position,
            "type": "statTest"
        }
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()

    #function that sets the text of the drag column
    def calculateFunction(self):
        if self.columnLabel.getText() != "No column Selected" and self.columnLabel2.getText() != "No column Selected" :
            answer = self.function(self.columnLabel.getText(), self.columnLabel2.getText())
            self.answerLabel.setText(str(answer))
            self.answer = str(answer)
    #Defines what happens when the widget is dragged

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())


            drag.exec(Qt.DropAction.MoveAction)
    
    

