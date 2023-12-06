import sys

from PyQt5.QtWidgets import QApplication,QLabel, QWidget,QPushButton,QHBoxLayout,QGridLayout

app=QApplication([])

window=QWidget()
window.setWindowTitle("DataAnalysis")
window.setGeometry(100,100,280,80)

layout=QGridLayout()

layout.addWidget(QPushButton("B1"),0,0)
layout.addWidget(QPushButton("B2"),0,1)
layout.addWidget(QPushButton("B3"),0,2)

layout.addWidget(QPushButton("B4"),1,0)
layout.addWidget(QPushButton("B5"),1,1)
layout.addWidget(QPushButton("B6"),1,2)


layout.addWidget(QPushButton("B7"),2,0)
layout.addWidget(QPushButton("B8"),2,1,1,2)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
