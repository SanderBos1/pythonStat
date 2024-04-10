from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from customWidgets import descriptiveCreatedWidget
from customWidgets.statTestCreatedWidget import statTestCreatedWidget
from PyQt6.QtCore import Qt

class userDashboard(QWidget):
    def __init__(self,  *args, **kwargs):
        super(userDashboard, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.createdWidgets = []
        self.userDashboardLayout = QHBoxLayout()
        self.insertedWidgetLayout = QVBoxLayout()

        self.userDashboardLayout.addLayout(self.insertedWidgetLayout)

        self.setLayout(self.userDashboardLayout)

    def getState(self):
        """
        Returns a list that corresponds to all the widgets that a user has created and their corresponding state data
        This list is used to save the user state
        """
        stateInformation = [None]*len(self.createdWidgets)
        for widget in self.createdWidgets:
            position = widget.getPosition()
            stateInformation[position] = widget.getData()

        return stateInformation

    def setState(self, createdWidgetsList):
        """
        Creates the state that was saved from the created widget list.
        The created widget list contains dictionaries which correspond to created widgets and their corresponding values.
        These values can be used to create the widgets again and give them the value they had before.
        """
        for createdWidget in createdWidgetsList:
            if createdWidget["type"] == "descriptive":
                self.addDescriptiveLabel(createdWidget['text'], createdWidget['function'], createdWidget['answer'], createdWidget['column'])
            elif createdWidget["type"] == "statTest":
                self.addStatLabel(createdWidget['text'], createdWidget['function'], createdWidget['column'], createdWidget['column2'],  createdWidget['answer'])

    def dragEnterEvent(self, e):
        """Lets the widget accept drag events"""

        e.accept()


    def dropEvent(self, e):
        """ 
        This drop event enables the user to change the order of widgets created by the user.
        It compares the position of the dropped widget with those still placed in the layout.
        It places the dropped widget below the widget with a smaller x-value, starting from the lowest x-value.

        Then it resets the positions to remember the order in which the widgets are placed.
        """
        widget = e.source()
        if isinstance(widget, descriptiveCreatedWidget):        
            position = e.position()
            self.insertedWidgetLayout.removeWidget(widget)
            for n in range(self.insertedWidgetLayout.count()):
                w = self.insertedWidgetLayout.itemAt(n).widget()
                if position.y() < w.y():
                    break
            else:
                n+=1
            self.insertedWidgetLayout.insertWidget(n, widget)
            widget.setPosition(n)
            
            for n in range(self.insertedWidgetLayout.count()):
                w = self.insertedWidgetLayout.itemAt(n).widget()
                w.setPosition(n)
            e.accept()

    def addDescriptiveLabel(self, name, function, answer = None, column = None):

        """
        Adds a descriptive label to the user dashboard.
        It has the following parameters:

        name: The name of the function associated with this label.
        function: The actual function associated with this label.
        position: Where it is placed in the array of widgets.

        Optional parameters:
        column: Sets the text of the label which displays which column is associated with it.
        answer: Sets the text of the label which displays the results of the calculation.
        """
        position = len(self.createdWidgets)
        if answer == None and column == None:
            label = descriptiveCreatedWidget(name, function, position)
        else:
            label = descriptiveCreatedWidget(name, function, position, answer, column)
        self.createdWidgets.append(label)
        self.insertedWidgetLayout.addWidget(label)
  


    def addStatLabel(self, name,  function, column = None, column2 = None, answer = None):

        """
        Adds a stat label to the user dashboard.
        It has the following parameters:

        name: The name of the function associated with this label.
        function: The actual function associated with this label.
        position: Where it is placed in the array of widgets.

        Optional parameters:
            column: Sets the text of the label which displays which column is associated with it.
            column2: Sets the text of the second label which displays which column is associated with it.
            answer: Sets the text of the label which displays the results of the calculation.
        """
        position = len(self.createdWidgets)
        if answer == None and column == None and column2 == None:
            label = statTestCreatedWidget(name, function, position)
        else:
            label = statTestCreatedWidget(name, function, position, column, column2, answer)
            
        self.createdWidgets.append(label)
        
        self.insertedWidgetLayout.addWidget(label)
