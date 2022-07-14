# 动画实验


import sys

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import pandas as pd
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)

    def compute_initial_figure(self):
        pass


class AnimationWidget(QtWidgets.QWidget):
    flag = 0
    data0 = pd.read_excel('原始数据.xlsx')
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        vbox = QtWidgets.QVBoxLayout()
        self.canvas = FigureCanvas(plt.Figure(figsize=(15,6)))
        self.ax=self.canvas.figure.subplots()
        vbox.addWidget(self.canvas)
        self.ax.set_ylim([0,100])

        hbox = QtWidgets.QHBoxLayout()
        self.start_button = QtWidgets.QPushButton("start", self)
        self.label1=QtWidgets.QLabel("label1",self)
        self.label2 = QtWidgets.QLabel("label2", self)
        self.stop_button = QtWidgets.QPushButton("stop", self)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.stop_button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.p = 0



        self.x0 = AnimationWidget.data0.Time
        self.x = np.linspace(0, 100, 100)
        self.y0 = AnimationWidget.data0.force
        self.y = np.linspace(-1, 4000, 100)
        self.ax.plot(self.x, self.y)



    # def update_line(self, i):
    #     if (120 + self.p) <= AnimationWidget.data0.shape[0]:
    #         self.p += 6
    #     y = self.y0[self.p:100 + self.p]
    #     t = self.x0[self.p]
    #     f = self.y0[self.p]
    #     self.line.set_ydata(y)
    #     self.label1.setText(f'{t}{f}')
    #     return [self.line]
    #
    # def on_start(self):
    #     if AnimationWidget.flag == 0:
    #         self.ani = FuncAnimation(self.canvas.figure, self.update_line,frames=10,blit=True, interval=0)
    #         AnimationWidget.flag = 1
    # def on_stop(self):
    #     if AnimationWidget.flag == 1:
    #         self.ani._stop()
    #         AnimationWidget.flag = 0


if __name__ == "__main__":
    qApp = QtWidgets.QApplication(sys.argv)
    aw = AnimationWidget()
    aw.show()
    sys.exit(qApp.exec_())
