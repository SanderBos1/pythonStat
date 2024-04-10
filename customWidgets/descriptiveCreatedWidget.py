from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel

class descriptiveCreatedWidget(QWidget):
    """
    Creates a widget that contains the following elements:

    functionLabel: A label that displays which function is calculated when a label is dropped into this widget.
    DeleteButton: When pressed, removes the widget from the window.
    columnLabel: Displays on which column of the dataset the function is calculated.
    answerLabel: Displays the answer of the calculation.

    Accepts drag events.
    """
    def __init__(self, text, function, position, answer = "", column = "No column Selected", *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.function = function
        self.text = text
        self.column = column
        self.answer = answer
        self.position = position

        self.widgetLayout = QVBoxLayout()
        self.informationLayout = QHBoxLayout()

        self.interactionLayout = QHBoxLayout()
        self.interactionLayout.addStretch(1)


        deleteButton = QPushButton()
        deleteButton.setText("X")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.column)

        self.functionLabel = QLabel()
        self.functionLabel.setText(self.text)

        
        self.answerLabel = QLabel()
        self.answerLabel.setText(self.answer)
        
        self.informationLayout.addWidget(self.functionLabel)
        self.informationLayout.addWidget(self.columnLabel)
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
        Returns all information needed to recreate a descriptiveWidget
        Returns:
            A dictionary containing:
                function: The function that is associated with this widget
                Text: The name that is given to the widget, usually the function name
                Column: The dataset column that is associated with it
                Answer: If their is already a calculation made, its answer will be saved here
                Type: A string so that the program can read which widget has to be created.

        """

        return {
            "function":self.function, 
            "text": self.text,
            "column":self.column, 
            "answer": self.answer,
            "type": "descriptive"
        }
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()

    #function that calculate and sets the answer
    def calculateFunction(self):
        self.column = self.columnLabel.getText()
        answer = self.function(self.columnLabel.getText())
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
