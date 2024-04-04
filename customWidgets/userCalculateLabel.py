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
    def __init__(self, text, function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

        #sets the width and hide of the widget
        width = 200
        height = 200
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.function = function

        self.widgetLayout = QGridLayout()

        functionLabel = QLabel(text)

        self.columnLabel = QLabel("No column selected")
        self.calculationAnswerLabel = QLabel("No column selected")

        deleteButton = QPushButton()
        deleteButton.setText("Remove")      
        deleteButton.setIcon(QIcon("close.png"))
        deleteButton.clicked.connect(self.deleteElement)

        
        self.widgetLayout.addWidget(functionLabel, 0, 0, 1, 2)
        self.widgetLayout.addWidget(deleteButton, 0, 3)
        self.widgetLayout.addWidget(self.columnLabel, 1, 0)
        self.widgetLayout.addWidget(self.calculationAnswerLabel, 1, 1)


        self.setLayout(self.widgetLayout)

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

        self.columnLabel = QLabel(widget.getText())

        self.calculationAnswerLabel = QLabel(str(self.function(widget.getText())))

        self.widgetLayout.addWidget(self.columnLabel)
        self.widgetLayout.addWidget(self.calculationAnswerLabel)


