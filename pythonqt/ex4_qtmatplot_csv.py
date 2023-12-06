#https://www.pythonguis.com/tutorials/plotting-matplotlib/
import sys
import matplotlib
from pathlib import Path
import random
matplotlib.use('Qt5Agg')
import pandas as pd
import numpy as np

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

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

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
        layout.addWidget(self.sc)

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
            self.update_plot(str(path))   

    def update_plot(self,filename):
        a=pd.read_csv(filename, skiprows=lambda x: (x != 0) and not x % 2)
        df=a.iloc[:,2]
        #df=a.iloc[start:end,2]
        fft_data=df.to_numpy()
        filtered1=fft_data/32767
        Fs = 300e3        # Sampling frequency in Hz
        Fc = 100e3         # Cutoff frequency in Hz (adjust as needed)
        #alpha = 2 * np.pi * Fc / Fs  # Filter coefficient
        alpha=0.5825
        print("alpha : ",alpha)
        filtered=self.first_order_lowpass(filtered1,alpha)
        '''        
        for j in range(fft_data.shape[0]):
            if fft_data[j] > 14000:
                if j == 0:
                    fft_data[0]=0
                else:    
                    fft_data[j]=fft_data[j-1]     
        '''
        self.sc.axes.cla()
        self.sc.axes.plot(filtered)
        self.sc.draw()
        #self.canvas.axes.cla()  # Clear the canvas.
        #self.canvas.axes.plot(fft_data, 'r')
        # Trigger the canvas to update and redraw.
        #self.canvas.draw()


    def first_order_lowpass(self,x, alpha):
        y = np.zeros_like(x)
        y[0] = x[0]
        for i in range(1, len(x)):
            y[i] = alpha * x[i] + (1 - alpha) * y[i - 1]
        return y
    

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()