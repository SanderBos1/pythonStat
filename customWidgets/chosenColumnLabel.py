from PyQt6.QtWidgets import QLabel
from customWidgets.datasetColumnLabel import datasetColumnLabel


class chosenColumnLabel(QLabel):
    """
    Defines a lobal that functions as a drop off point for the column label
    """
    def __init__(self, calculateFunction, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.calculateFunction = calculateFunction


    def getText(self):
        return self.text() 
    
    def dropEvent(self, e):
        """ Defines what happens if a widget gets droped in this widget"""
        widget = e.source()
        if isinstance(widget, datasetColumnLabel):
            self.setText(widget.getText())
            self.calculateFunction()

    def dragEnterEvent(self, e):
        """Lets the widget accept drag events"""

        e.accept()