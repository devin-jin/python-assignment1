


import sys
from PyQt5 import QtWidgets,QtCore,QtGui
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
        self.setParent(parent)

    def compute_initial_figure(self):
        pass




class Ui_MainWindow(QtWidgets.QWidget):

    flag = 0
    data0 = pd.read_excel('原始数据.xlsx')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 201, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartButton.setFont(self.SetFont())
        self.StartButton.setObjectName("StartButton")
        self.verticalLayout.addWidget(self.StartButton)
        self.StartButton.clicked.connect(self.on_start)

        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StopButton.setFont(self.SetFont())
        self.StopButton.setObjectName("StopButton")
        self.verticalLayout.addWidget(self.StopButton)
        self.StopButton.clicked.connect(self.on_stop)

        # self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        # self.tableView.setFont(self.SetFont())
        # self.tableView.setObjectName("tableView")
        # self.verticalLayout.addWidget(self.tableView)
        self.tableView_init()
        self.tableView_add()

        self.EditButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EditButton.setFont(self.SetFont())
        self.EditButton.setObjectName("EditButton")
        self.verticalLayout.addWidget(self.EditButton)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(260, 300, 901, 441))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        ####







        self.label1 = QtWidgets.QLabel("label1", self)
        self.label2 = QtWidgets.QLabel("label2", self)
        self.label1.setText('Time: 0')
        self.label2.setText('Force: 0')
        self.label1.setFont(self.SetFont())
        self.label2.setFont(self.SetFont())

        self.verticalLayout.addWidget(self.label1)
        self.verticalLayout.addWidget(self.label2)







        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(260, 20, 451, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tableView_2 = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        self.tableView_2.setFont(self.SetFont())
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_2.addWidget(self.tableView_2)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(740, 20, 421, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.canvas = MyMplCanvas(self, width=8, height=6, dpi=100)
        self.verticalLayout_3.addWidget(self.canvas)
        self.p = 0

        self.x0 = Ui_MainWindow.data0.Time
        self.x = np.linspace(0, 100, 100)
        self.y0 = Ui_MainWindow.data0.force
        self.y = np.linspace(-1, 4000, 100)
        self.line, = self.canvas.axes.plot(self.x, self.y, animated=True, lw=2)

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Input Start"))
        self.StopButton.setText(_translate("MainWindow", "Input Pause"))
        self.EditButton.setText(_translate("MainWindow", "Eidt User\'s Profile"))

    def SetFont(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        return font

    def update_line(self, i):
        if (120 + self.p) <= Ui_MainWindow.data0.shape[0]:
            self.p += 2
        y = self.y0[self.p:100 + self.p]
        t = self.x0[self.p]
        f = self.y0[self.p]
        self.line.set_ydata(y)
        self.label1.setText(f'Time: {t}')
        self.label2.setText('Force: %.3f'%f)
        return [self.line]

    def on_start(self):
        if Ui_MainWindow.flag == 0:
            self.ani = FuncAnimation(self.canvas.figure, self.update_line, frames=10, blit=True, interval=0)
            Ui_MainWindow.flag = 1

    def on_stop(self):
        if Ui_MainWindow.flag == 1:
            self.ani._stop()
            Ui_MainWindow.flag = 0


    def tableView_init(self):
        # 创建一个 0行3列 的标准模型
        self.model = QtGui.QStandardItemModel(0, 2)
        # 设置表头标签
        # self.model.setHorizontalHeaderLabels(['姓名', '年龄', '年薪'])

        self.tableview = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableview.setFont(self.SetFont())
        self.tableview.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableview)

        # 创建 tableView 组件
        # 将 tableView 添加到垂直盒布局里

        # tableView 组件 设置模型
        self.tableview.setModel(self.model)

        self.tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableview.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置只能选中整行
        self.tableview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 不可编辑
        self.tableview.setSelectionBehavior(QtWidgets. QAbstractItemView.SelectRows)  # 设置只能选中一行

        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        # self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行

    def tableView_add(self):
        print('a')
        # 写全
        item1 = QtGui.QStandardItem('%s' % '小朱')
        item2 = QtGui.QStandardItem('%s' % '21')
        print('b')
        self.model.appendRow([item1, item2])
        print('c')
        # 简写
        self.model.appendRow([
            QtGui.QStandardItem('%s' % '小明'),
            QtGui.QStandardItem('%s' % '20')
        ])
        print('d')

    def tableView_del_low(self):
        index = self.tableview.currentIndex()  # 取得当前选中行的index
        self.model.removeRow(index.row())  # 通过index的row()操作得到行数进行删除

    def tableView_clear(self):
        # 会全部清空，包括那个标准表头
        self.model.clear()
        # 所以重新设置标准表头 自己将一下代码注释 尝试
        self.model.setHorizontalHeaderLabels(['姓名', '年龄', '年薪'])






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
