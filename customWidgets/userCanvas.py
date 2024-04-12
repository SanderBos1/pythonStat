from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea
from statWidgets import descriptiveWidget, ttestWidget, normalityWidget
from PyQt6.QtCore import Qt

class userCanvas(QWidget):
    """
    Creates the widget where user created widgets are placed & their corresponding interactions
    """
    def __init__(self,  *args, **kwargs):
        super(userCanvas, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.createdWidgets = []

        
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)  # Allow the scroll area to resize its contents dynamically

        # Create a placeholder widget to hold the scrollable content
        scrollPlaceholder = QWidget()
        self.scrollArea.setWidget(scrollPlaceholder)

        # Create a layout for the scrollable content
        self.scrollLayout = QVBoxLayout(scrollPlaceholder)
        #makes sure widgets are added at the top
        self.scrollLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Set up the layout for the userDashboard widget
        dashboardLayout = QHBoxLayout(self)
        dashboardLayout.addWidget(self.scrollArea)

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
                self.addDescriptiveWidget(createdWidget['position'], createdWidget['column'])
            elif createdWidget["type"] == "statTest":
                self.addTtestWidget(createdWidget['position'], createdWidget['column'], createdWidget['column2'])
            elif createdWidget["type"] == "normal":
                self.addNormalityWidget(createdWidget['position'], createdWidget['column'])

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
        allowed = [descriptiveWidget, ttestWidget, normalityWidget]
        widget = e.source()
        if any(isinstance(widget, allowedWidget) for allowedWidget in allowed):        
            position = e.position()
            self.scrollLayout.removeWidget(widget)
            for n in range(self.scrollLayout.count()):
                w = self.scrollLayout.itemAt(n).widget()
                if position.y() < w.y():
                    break
            else:
                n+=1
            self.scrollLayout.insertWidget(n, widget)
            widget.setPosition(n)
            
            for n in range(self.scrollLayout.count()):
                w = self.scrollLayout.itemAt(n).widget()
                w.setPosition(n)
            e.accept()

    def addDescriptiveWidget(self, position=None, column = "No column selected"):

        if position == None:
            position = len(self.createdWidgets)
        
        
        label = descriptiveWidget(position, column)

        self.createdWidgets.append(label)
        self.scrollLayout.addWidget(label)
  


    def addTtestWidget(self, position = None, column = "No column Selected", column2 = "No column Selected"):

        """
        Adds a stat label to the user dashboard.
        It has the following parameters:

        position: Where it is placed in the array of widgets.

        Optional parameters:
            column: Sets the text of the label which displays which column is associated with it.
            column2: Sets the text of the second label which displays which column is associated with it.
        """
        if position == None:
            position = len(self.createdWidgets)
        
        label = ttestWidget(position, column, column2)
            
        self.createdWidgets.append(label)
        self.scrollLayout.addWidget(label)

    def addNormalityWidget(self, position=None, column = "No column selected"):

        if position == None:
            position = len(self.createdWidgets)
        
        
        label = normalityWidget(position, column)

        self.createdWidgets.append(label)
        self.scrollLayout.addWidget(label)