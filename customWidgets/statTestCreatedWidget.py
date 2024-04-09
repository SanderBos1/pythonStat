from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from customWidgets.chosenColumnLabel import chosenColumnLabel

class statTestCreatedWidget(QWidget):
    """
    Creates a widget that contains the following elements:

        functionLabel = A label that display which function is calculated when a label is droped into this widget
        DeleteButton = When pressed, removes the widget from the window
        columnLabel = Displays on which column of the dataset the function is calculated
        calculationAnswerLabel = Displays the answer of the calculation.

        Accepts drag events
    """
    def __init__(self, name, function, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.startText = "No column Selected"

        self.name = name
        self.function = function
        self.column = self.startText 
        self.column2 = self.startText 
        self.answer = ""

        self.widgetLayout = QHBoxLayout()



        deleteButton = QPushButton()
        deleteButton.setText("Remove")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        self.columnLabel = chosenColumnLabel(self.calculateFunction)
        self.columnLabel.setText(self.startText )

        self.columnLabel2 = chosenColumnLabel(self.calculateFunction)
        self.columnLabel2.setText(self.startText )
        
        self.answerLabel = QLabel()
        
        self.widgetLayout.addWidget(self.columnLabel)
        self.widgetLayout.addWidget(self.columnLabel2)

        self.widgetLayout.addWidget(self.answerLabel)
        self.widgetLayout.addWidget(deleteButton)

        self.setLayout(self.widgetLayout)

        self.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )

    def getInfo(self):
        return [self.columnLabel.getText() , self.columnLabel2.getText()]

    def getData(self):
        """ 
        Returns all information needed to recreate the object
        """
        return {
            "function":self.function, 
            "column":self.columnLabel.getText(), 
            "column2": self.columnLabel2.getText(),
            "answer": self.answer,
            "position": [int(self.x()), int(self.y())]
        }
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()

    #function that sets the text of the drag column
    def calculateFunction(self):
        if self.columnLabel.getText() != self.startText and self.columnLabel2.getText() != self.startText :
            answer = self.function(self.columnLabel.getText(), self.columnLabel2.getText())
            self.answerLabel.setText(str(answer))
            self.answer = answer
    #Defines what happens when the widget is dragged

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())


            drag.exec(Qt.DropAction.MoveAction)
    
    
    #Defines a hint of the size of the widget, can be compined with Qsizepolicy to determine how large the widget will be
    def sizeHint(self):
        return QSize(40,120)
