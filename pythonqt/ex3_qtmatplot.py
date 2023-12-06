#https://www.pythonguis.com/tutorials/plotting-matplotlib/
import sys
import matplotlib
from pathlib import Path
import random
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import (QLineEdit,QPushButton,
                             QHBoxLayout,QGridLayout,
                             QLabel,
                             QFileDialog)


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        #mainLayout=QGridLayout()
        layoutH1=QHBoxLayout()

        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        layoutH1.addWidget(QLabel('File:'))
        layoutH1.addWidget(self.filename_edit)
        layoutH1.addWidget(file_browse)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layoutH1)
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "./", 
            "CSV (*.csv *.bin)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path)) 
            self.update_plot()   

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:]  + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()