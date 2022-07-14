import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键

    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, self.fig) # 初始化父类
        self.setParent(parent)

        # self.fig,self.axes = plt.subplot()

        self.axes = self.fig.add_subplot(111)# 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
    def test(self):
        x = np.arange(0, 2 * np.pi, 0.01)
        self.axes.plot(x, np.sin(x))
class Ui_Main(object):
    def setupUi(self, Login):
        Login.setObjectName("Register")
        Login.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(120, 320, 90, 30))

        self.graphicview = QtWidgets.QWidget(Login)
        self.graphicview.setObjectName("graphicview")
        self.graphicview = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicview.setGeometry(QtCore.QRect(10, 10, 500, 200))

        dr = Figure_Canvas()
        # 实例化一个FigureCanvas
        dr.test()  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicview.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicview.show()  # 最后，调用show方法呈现图形！Voila!!
        # self.setCentralWidget(self.graphicview)

        # self.graphicview.setFixedSize(1000, 600)

        Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        #self.Register.clicked.connect(pass)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.Register.setText(_translate("Login", "Register"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui3 = Ui_Main()
    ui3.setupUi(Main)
    Main.show()
    app.exec_()