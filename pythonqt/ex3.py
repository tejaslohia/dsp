import sys

from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout)

app=QApplication([])

window=QWidget()
window.setWindowTitle("DataAnalysis")
window.setGeometry(100,100,280,80)

#layout=QHBoxLayout()
layout=QGridLayout()
layoutV1=QVBoxLayout()
layoutV2=QVBoxLayout()
#layout.addChildLayout(layoutV1)
#layout.addChildLayout(layoutV2)

layoutV1.addWidget(QPushButton("Left"))
layoutV1.addWidget(QPushButton("Middle"))
layoutV1.addWidget(QPushButton("Right"))

layoutV2.addWidget(QPushButton("Left"))
layoutV2.addWidget(QPushButton("Middle"))
layoutV2.addWidget(QPushButton("Right"))

layout.addLayout(layoutV1,0,0)
layout.addLayout(layoutV2,0,1)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
