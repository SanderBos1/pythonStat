from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QToolBar, QMenu, QPushButton
from customWidgets import disiplayCalculationElement, dragLabel
from statFunctions import mean, variance

class calculateWindow(QWidget):
    def __init__(self, df, *args, **kwargs):
        super(calculateWindow, self).__init__(*args, **kwargs)
        self.df = df

        self.toolsLayout = QVBoxLayout()
        self.explorationLayout = QGridLayout()
        self.createdWidgetLayout = QHBoxLayout()
        self.columnLayout = QVBoxLayout()
        pageLayout = QHBoxLayout()

        pageLayout.addLayout(self.columnLayout)
        self.toolsLayout.addLayout(self.explorationLayout)
        pageLayout.addLayout(self.toolsLayout)
        pageLayout.addLayout(self.createdWidgetLayout)    

        self.setLayout(pageLayout)
        self.createToolbar()
        self.showColumns()


    def createToolbar(self):

        meanButton = QPushButton("Mean")
        meanButton.clicked.connect(lambda: self.addLabel("mean", mean))

        VarianceButton = QPushButton("Variance")
        VarianceButton.clicked.connect(lambda: self.addLabel("Variance", variance))


        self.explorationLayout.addWidget(meanButton)
        self.explorationLayout.addWidget(VarianceButton)

    def showColumns(self):
        if self.df is not None:
            for column in self.df.columns:
                    label = dragLabel(str(column))
                    self.columnLayout.addWidget(label)

    def addLabel(self, name, function):
        label = disiplayCalculationElement(name, self.df, function)
        self.createdWidgetLayout.addWidget(label)


