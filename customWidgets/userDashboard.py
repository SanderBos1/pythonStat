from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout
from customWidgets import descriptiveCreatedWidget
from customWidgets.statTestCreatedWidget import statTestCreatedWidget
from PyQt6.QtCore import Qt

class userDashboard(QWidget):
    def __init__(self,  *args, **kwargs):
        super(userDashboard, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.createdWidgets = []
        self.userDashboardLayout = QHBoxLayout()
        self.insertedWidgetLayout = QGridLayout()

        self.userDashboardLayout.addLayout(self.insertedWidgetLayout, 6)

        self.setLayout(self.userDashboardLayout)

    def getState(self):
        """
        Returns a list that corresponds to all the widgets that a user has created and their state data
        This list is used to save the user state
        """
        stateInformation = []
        for widget in self.createdWidgets:
            stateInformation.append(widget.getData())
        return stateInformation

    def setState(self, createdWidgetsList):
        """
        Creates a state from a list of dictionaries that corresponds to the previous created widgets
        """
        for createdWidget in createdWidgetsList:
            self.addDescriptiveLabel(createdWidget['text'], createdWidget['function'], createdWidget['column'], createdWidget['answer'], createdWidget['position'])

    def dragEnterEvent(self, e):
        """Lets the widget accept drag events"""

        e.accept()


    def dropEvent(self, e):
        """ Defines what happens if a widget gets droped in this widget"""
        widget = e.source()
        if isinstance(widget, descriptiveCreatedWidget):        
            position = e.position()
            widget.move(position.toPoint())

            e.setDropAction(Qt.DropAction.MoveAction)
            e.accept()

    def addDescriptiveLabel(self, name, function, column = "No column selected", answer = "No column selected", position = None):

        """
        Adds a label widget to the drawing frame which accept drag events
        On drag events it calculates it associated function on the column it receives.
        
        """
        label = descriptiveCreatedWidget(name, function, answer, self)
        self.createdWidgets.append(label)
        
        self.insertedWidgetLayout.addWidget(label)
        if position != None:
            label.move(position[0], position[1])


    def addStatLabel(self, name,  function,  position = None):

        """
        Adds a label widget to the drawing frame which accept drag events
        On drag events it calculates it associated function on the column it receives.
        
        """
        label = statTestCreatedWidget(name, function, self)
        self.createdWidgets.append(label)
        
        self.insertedWidgetLayout.addWidget(label)
        if position != None:
            label.move(position[0], position[1])