from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QMimeData, Qt
from PyQt6.QtGui import QDrag, QPixmap



class datasetColumnLabel(QLabel):
    """
    Defines a label that is dragable
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(40, 400, 100, 100)


    def getText(self):
        return self.text() 

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.MoveAction)