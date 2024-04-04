from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout,  QPushButton
from PyQt6.QtGui import QIcon


class disiplayCalculationElement(QWidget):
    """
    Creates a widget that contains the following elements:

        functionLabel = A label that display which function is calculated when a label is droped into this widget
        DeleteButton = When pressed, removes the widget from the window
        columnLabel = Displays on which column of the dataset the function is calculated
        calculationAnswerLabel = Displays the answer of the calculation.

        Accepts drag events
    """
    def __init__(self, text, function, column, answer,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

        #sets the width and hide of the widget
        width = 200
        height = 200
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.function = function
        self.text = text
        self.column = column
        self.answer = answer

        self.widgetLayout = QGridLayout()

        functionLabel = QLabel(self.text)

        self.columnLabel = QLabel(self.column )
        self.calculationAnswerLabel = QLabel(self.answer)

        deleteButton = QPushButton()
        deleteButton.setText("Remove")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        
        self.widgetLayout.addWidget(functionLabel, 0, 0, 1, 2)
        self.widgetLayout.addWidget(deleteButton, 0, 3)
        self.widgetLayout.addWidget(self.columnLabel, 1, 0)
        self.widgetLayout.addWidget(self.calculationAnswerLabel, 1, 1)


        self.setLayout(self.widgetLayout)

    def getData(self):
        """ 
        Returns all information needed to recreate the object
        """
        return {
            "function":self.function, 
            "text": self.text,
            "column":self.column, 
            "answer": self.answer}
    
    def deleteElement(self):
        """Function to delete the widget"""
        self.deleteLater()

    def dragEnterEvent(self, e):
        """Lets the widget accept drag events"""

        e.accept()

    def dropEvent(self, e):
        """ Defines what happens if a widget gets droped in this widget"""
        widget = e.source()
        self.widgetLayout.removeWidget(self.calculationAnswerLabel)
        self.widgetLayout.removeWidget(self.columnLabel)

        self.column = widget.getText()
        self.answer = str(self.function(widget.getText()))
        
        self.columnLabel = QLabel(self.column)
        self.calculationAnswerLabel = QLabel(self.answer)

        self.widgetLayout.addWidget(self.columnLabel)
        self.widgetLayout.addWidget(self.calculationAnswerLabel)


