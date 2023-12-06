import sys

from PyQt5.QtWidgets import QApplication,QHBoxLayout, QWidget,QPushButton,QLineEdit,QFormLayout

app=QApplication([])

window=QWidget()
window.setWindowTitle("DataAnalysis")
window.setGeometry(100,100,280,80)

layout=QFormLayout()
layout.addRow("Name : ",QLineEdit())
layout.addRow("Age : ",QLineEdit())
layout.addRow("Address : ",QLineEdit())
buttonLayout=QHBoxLayout()
buttonLayout.addWidget(QPushButton("OK"))
buttonLayout.addWidget(QPushButton("Cancel"))

layout.addRow(buttonLayout)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
