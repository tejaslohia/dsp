import sys

from PyQt5.QtWidgets import QApplication,QLabel, QWidget,QPushButton,QHBoxLayout

app=QApplication([])

window=QWidget()
window.setWindowTitle("DataAnalysis")
window.setGeometry(100,100,280,80)

layout=QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Middle"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
