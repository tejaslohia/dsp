import sys
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication,QVBoxLayout, QWidget,QPushButton,QLineEdit,QFormLayout,QDialog,QDialogButtonBox

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog Example")
        dialogLayout=QVBoxLayout()

        layout=QFormLayout()
        layout.addRow("Name : ",QLineEdit())
        layout.addRow("Age : ",QLineEdit())
        layout.addRow("Address : ",QLineEdit())

        dialogLayout.addLayout(layout)
        
        buttons=QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        dialogLayout.addWidget(buttons)

        self.setLayout(dialogLayout)



app=QApplication([])
window=Window()
window.show()
sys.exit(app.exec())
