from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout,QVBoxLayout,  QPushButton


class disiplayCalculationElement(QWidget):
    def __init__(self, text, df, function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

        self.df = df
        self.function = function

        widgetLayout = QVBoxLayout()
        self.customLayout = QHBoxLayout()
        self.answerLayout = QHBoxLayout()
        functionLabel = QLabel(text)
        self.calculationAnswerLabel = QLabel("No column selected")
        deleteButton = QPushButton()
        deleteButton.clicked.connect(self.deleteElement)

        
        self.customLayout.addWidget(functionLabel)
        self.customLayout.addWidget(deleteButton)
        self.answerLayout.addWidget(self.calculationAnswerLabel)

        widgetLayout.addLayout(self.customLayout)
        widgetLayout.addLayout(self.answerLayout)

        self.setLayout(widgetLayout)

    def deleteElement(self):
        self.deleteLater()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        widget = e.source()
        self.answerLayout.removeWidget(self.calculationAnswerLabel)
        self.calculationAnswerLabel = QLabel(str(self.function(self.df[widget.getText()])))
        self.answerLayout.addWidget(self.calculationAnswerLabel)


