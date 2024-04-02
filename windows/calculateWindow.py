from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QLabel
from PyQt6.QtGui import QAction
from statFunctions import mean
from pandas.api.types import is_numeric_dtype

class calculateWindow(QWidget):
    def __init__(self, parent=None):
        super(calculateWindow, self).__init__(parent)
            
        self.df = None
        menuLayout = QVBoxLayout()
        answerLayout = QVBoxLayout()
        self.columnDropDown = QComboBox()
        self.calculatedAnswer = QLabel()
        self.columnDropDown.currentTextChanged.connect(self.meanCalculator)

        menuLayout.addWidget(self.columnDropDown)
        answerLayout.addWidget(self.calculatedAnswer)
        pageLayout = QHBoxLayout()
        pageLayout.addLayout(menuLayout)    
        pageLayout.addLayout(answerLayout)

        self.setLayout(pageLayout)


    def updatedf(self, df):
        self.df = df

    
    def toolbox(self):
        self.columnDropDown.clear()
        for column in self.df.columns:
            self.columnDropDown.addItem(column)
        self.show()

    def meanCalculator(self, s):
        if self.df is not None and s in self.df.columns and is_numeric_dtype(self.df[s]):
            answer = mean(self.df[s])
        else:
            answer = "This column is not numerical"
        self.calculatedAnswer.setText(str(answer))
    
