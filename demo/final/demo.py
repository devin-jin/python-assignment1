import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


class parameter():
    G = 9.8
    Start_interval_Time = 500
    count1 = 1
    update_rate = 10


class io():
    userdata = pd.DataFrame()
    data0 = pd.DataFrame()
    parameter = pd.DataFrame()
    user = ''
    len_user = 0
    userid = 0

    @classmethod
    def read(cls, s):
        if s == 'user':
            io.userdata = pd.read_excel('userdata.xlsx')
            io.user = io.userdata.iloc[:, 0:2]
            io.len_user = io.user.shape[0]
        if s == 'data':
            io.data0 = pd.read_excel('原始数据.xlsx')

    @classmethod
    def write(cls, s):
        if s == 'user':
            io.userdata.to_excel('userdata.xlsx', index=False)
        if s == 'data':
            io.data0.to_excel('userdata.xlsx', index=False)
        if s == 'parameter':
            io.parameter.to_excel('parameter.xlsx', index=False)


class Ui_Login(object):

    def __init__(self):
        self.flag = 0

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.SignIn = QtWidgets.QPushButton(self.centralwidget)
        self.SignIn.setGeometry(QtCore.QRect(120, 250, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.SignIn.setFont(font)
        self.SignIn.setObjectName("SignIn")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(340, 250, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Register.setFont(font)
        self.Register.setObjectName("Register")
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setGeometry(QtCore.QRect(220, 90, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LineEdit.setFont(font)
        self.LineEdit.setObjectName("LineEdit")
        self.LineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_2.setGeometry(QtCore.QRect(220, 160, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 90, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 500, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.SignIn.clicked.connect(self.check)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.SignIn.setText(_translate("Login", "Sign In"))
        self.Register.setText(_translate("Login", "Register"))
        self.label.setText(_translate("Login", "Username:"))
        self.label_2.setText(_translate("Login", "Password:"))

    def check(self):
        username = self.LineEdit.text()
        password = self.LineEdit_2.text()

        io.read('user')
        flag1 = 1
        for i in range(io.len_user):
            if io.user.iloc[i].user == username and io.user.iloc[i].password == password:
                self.flag = 1
                flag1 = 0
                self.label_3.setGeometry(QtCore.QRect(230, 210, 500, 21))
                io.userid = i
                Name = io.userdata.iloc[io.userid, 2]
                self.label_3.setText(f'Welcome.{Name}')

        if flag1 == 1:
            self.label_3.setText('Your username or password is incorrect. Please try again.')


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(120, 320, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Register.setFont(font)
        self.Register.setObjectName("Register")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(340, 320, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Quit.setFont(font)
        self.Quit.setObjectName("Quit")
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setGeometry(QtCore.QRect(300, 90, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LineEdit.setFont(font)
        self.LineEdit.setObjectName("LineEdit")
        self.LineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_2.setGeometry(QtCore.QRect(300, 160, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.LineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit_3.setGeometry(QtCore.QRect(300, 230, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LineEdit_3.setFont(font)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 280, 500, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText(" ")
        self.label_4.setObjectName("label_4")
        Register.setCentralWidget(self.centralwidget)
        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        self.Register.clicked.connect(self.CheckRegister)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.Register.setText(_translate("Login", "Register"))
        self.Quit.setText(_translate("Login", "Cancel"))
        self.label.setText(_translate("Login", "New Username:"))
        self.label_2.setText(_translate("Login", "New Password:"))
        self.label_3.setText(_translate("Login", "Retry new Password:"))

    def CheckRegister(self):
        username = self.LineEdit.text()
        password = self.LineEdit_2.text()
        confirm_password = self.LineEdit_3.text()
        io.read('user')
        if password != confirm_password:
            self.label_4.setText('Password and confirm password do not match.')
            self.label_4.setGeometry(QtCore.QRect(100, 280, 500, 21))
        else:
            flag2 = 1
            for i in range(io.len_user):
                if io.userdata.iloc[i, 0] == username:
                    self.label_4.setGeometry(QtCore.QRect(180, 280, 300, 21))
                    self.label_4.setText('This username is occupied')
                    flag2 = 0
                    break
            if flag2 == 1 and len(password) < 6:
                self.label_4.setGeometry(QtCore.QRect(130, 280, 500, 21))
                self.label_4.setText('Password must be at least 6 characters. ')
                flag2 = 0
            if flag2 == 1:
                self.label_4.setGeometry(QtCore.QRect(200, 280, 300, 21))
                self.label_4.setText('Registration successful.')
                io.userdata.loc[io.len_user] = [username, password, 'Unknown', 'Unknown', 'Unknown', 'Unknown',
                                                'Unknown']
                io.write('user')


class MyMplCanvas(FigureCanvas):
    """创建了一个widget"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def compute_initial_figure(self):
        pass


class Ui_MainWindow(QtWidgets.QWidget):
    flag = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 350, 500))
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

        self.tableView_init(0)

        self.EditButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EditButton.setFont(self.SetFont())
        self.EditButton.setObjectName("EditButton")
        self.verticalLayout.addWidget(self.EditButton)

        self.PasswordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.PasswordButton.setFont(self.SetFont())
        self.PasswordButton.setObjectName("PasswordButton")
        self.verticalLayout.addWidget(self.PasswordButton)

        self.ExportParameterButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ExportParameterButton.setFont(self.SetFont())
        self.ExportParameterButton.setObjectName("ExportParameterButton")
        self.verticalLayout.addWidget(self.ExportParameterButton)
        self.ExportParameterButton.clicked.connect(self.export)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 540, 1760, 440))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label1 = QtWidgets.QLabel("label1", self)
        self.label1.setText('Time: 0.000     Force: 0.000')
        self.label1.setFont(self.SetFont())

        self.verticalLayout.addWidget(self.label1)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 20, 480, 500))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tableView_init(1)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(880, 20, 890, 500))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.draw()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SetFont(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        return font

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Input Start"))
        self.StopButton.setText(_translate("MainWindow", "Input Pause"))
        self.EditButton.setText(_translate("MainWindow", "Edit Profile"))
        self.PasswordButton.setText(_translate("MainWindow", "Change Password"))
        self.ExportParameterButton.setText(_translate("MainWindow", "Export Parameter"))

    def draw(self):
        self.canvas = MyMplCanvas(self, width=8, height=6, dpi=100)
        self.verticalLayout_3.addWidget(self.canvas)
        self.p = 0

        io.read('data')
        self.x0 = io.data0.Time
        self.x = np.linspace(0, 100, 100)
        self.y0 = io.data0.force
        self.y = np.linspace(-1, 4000, 100)
        self.line, = self.canvas.axes.plot(self.x, self.y, animated=True, lw=1)

        self.flag = 0
        self.listP = []
        self.body_weight = 0
        self.i = 0

    def diff(self, i):
        return abs(self.y0[self.p] - self.y0[self.p + i]) < 100

    def update_line(self, i):
        if (120 + self.p) <= io.data0.shape[0]:
            self.p += parameter.update_rate
        y = self.y0[self.p:100 + self.p]
        t = self.x0[self.p]
        f = self.y0[self.p]

        if self.flag == 0 and self.y0[self.p] > 100 and (self.y0[self.p] - self.y0[self.p + 50]) > 100:
            self.listP.append(self.p)
            self.i += 1
            self.flag = 1

        if self.flag == 1 and self.y0[self.p] > 100 and self.diff(200) and self.diff(100) and self.diff(50):
            self.listP.append(self.p)
            self.draw2(self.i)
            self.flag = 0

        self.line.set_ydata(y)
        self.label1.setText('Time: %5.3f     Force: %5.3f ' % (t, f))
        return [self.line]

    def draw2(self, i):
        self.x = self.x0[self.listP[2 * i - 2] - 200:self.listP[2 * i - 1] + 200]
        self.y = self.y0[self.listP[2 * i - 2] - 200:self.listP[2 * i - 1] + 200]
        self.canvas2 = FigureCanvas(plt.Figure(figsize=(8, 6)))
        self.ax = self.canvas2.figure.subplots()
        self.horizontalLayout_3.addWidget(self.canvas2)
        self.ax.plot(self.x, self.y)

        self.parameter(i)
        self.draw_line()
        self.tableView_add(1)
        self.export_parameter(i)

        self.ax.set_title(f'Jump {i}')
        self.ax.set_xlabel('Time[s]')
        self.ax.set_ylabel('Ground reaction force[N]')
        self.canvas2.figure.savefig(f'Jump {i}.jpg')

    def draw_line(self):
        self.take_off_time = self.flight.iloc[0, 0]
        self.landing_time = self.flight.iloc[-1, 0]
        self.start = self.period.iloc[0, 0]

        self.ax.plot([self.start - 0.02] * 2, [self.period.iloc[0, 1], 2700], '--', color='gray', lw=1)
        self.ax.annotate('Start', xy=(self.start - 0.02, self.period.iloc[0, 1]), fontsize=8,
                         xytext=(self.start - 0.15, self.period.iloc[0, 1] - 500),
                         arrowprops=dict(facecolor='gray', arrowstyle='->'))

        self.ax.plot([self.take_off_time] * 2, [0, 2700], '--', color='gray', lw=1)
        self.ax.annotate('Take Off', xy=(self.take_off_time, 0), fontsize=8,
                         xytext=(self.take_off_time - 0.40, 100),
                         arrowprops=dict(facecolor='gray', arrowstyle='->'))

        self.ax.plot([self.landing_time] * 2, [0, 2700], '--', color='gray', lw=1)
        self.ax.annotate('Landing', xy=(self.landing_time, 0), fontsize=8,
                         xytext=(self.landing_time + 0.15, 100),
                         arrowprops=dict(facecolor='gray', arrowstyle='->'))

        self.ax.plot([self.low_index / 1000] * 2, [self.low_force, 2300], '--', color='gray', lw=1)
        self.ax.plot([self.peak_index / 1000] * 2, [self.peak_force, 2700], '--', color='gray', lw=1)

        self.ax.annotate('', xy=(self.start - 0.02, 2700),
                         xytext=(self.peak_index / 1000, 2700),
                         arrowprops=dict(facecolor='gray', arrowstyle='<->'))
        self.ax.annotate('', xy=(self.peak_index / 1000, 2700),
                         xytext=(self.take_off_time, 2700),
                         arrowprops=dict(facecolor='gray', arrowstyle='<->'))
        self.ax.annotate('', xy=(self.take_off_time, 2700),
                         xytext=(self.landing_time, 2700),
                         arrowprops=dict(facecolor='gray', arrowstyle='<->'))
        self.ax.annotate('', xy=(self.low_index / 1000, 2300),
                         xytext=(self.peak_index / 1000, 2300),
                         arrowprops=dict(facecolor='gray', arrowstyle='<->'))
        self.ax.annotate('Braking', xy=(self.peak_index / 1000 - 0.2, 2400), fontsize=8)
        self.ax.annotate('Counter\nMovement', xy=(self.peak_index / 1000 - 0.33, 2800), fontsize=8)
        self.ax.annotate('Push Off', xy=(self.take_off_time - 0.26, 2800), fontsize=8)
        self.ax.annotate('Flight', xy=(self.landing_time - 0.27, 2800), fontsize=8)

    def parameter(self, i):
        self.flag2 = 0
        self.flag3 = 0
        self.t1 = 0
        self.t2 = 0
        self.peak_force = 0
        self.peak_index = 0
        self.low_force = 1000
        self.low_index = 0
        self.last_peak_time = 0
        self.count1 = 0
        self.count2 = 0
        self.body_weight = np.average(io.data0.iloc[self.listP[2 * i - 2] - 200:self.listP[2 * i - 2] - 100, 1])
        self.period = io.data0[self.listP[2 * i - 2]:self.listP[2 * i - 1]]

        for i in range(self.listP[2 * i - 2], self.listP[2 * i - 1]):
            f = io.data0.iloc[i, 1]
            t = io.data0.iloc[i, 0]
            if f > self.peak_force and self.flag2 == 0:
                self.peak_force = f
                self.peak_index = i
            else:
                self.count1 += 1
            if self.count1 == 500:
                self.flag2 = 1

            if f < self.low_force and self.flag3 == 0:
                self.low_force = f
                self.low_index = i
            else:
                self.count2 += 1
            if self.count2 == 100:
                self.flag3 = 1

        self.body_mass = self.body_weight / parameter.G
        self.flight = self.period[self.period.force < 4]
        self.flight_T = self.flight.shape[0] / 1000
        self.jump_T = self.flight.iloc[0, 0] - self.period.iloc[0, 0]
        self.jump_height_from_flight_T = parameter.G * (self.flight_T / 2) ** 2 / 2
        self.start_interval = io.data0[self.peak_index:self.peak_index + parameter.Start_interval_Time]
        self.Start_interval_relative_F = np.average(self.start_interval.iloc[:, 1] / self.body_weight)
        self.relative_max_F = self.peak_force / self.body_weight
        self.start_interval_A = np.average(self.start_interval.iloc[:, 1] / self.body_mass) - parameter.G

    def export_parameter(self, i):
        if i == 1:
            io.parameter = pd.DataFrame(columns=self.parameter_list)
        io.parameter.loc[i - 1] = self.value_list

    def export(self):
        if io.parameter.shape[1] == 7:
            io.write('parameter')

    def on_start(self):
        if Ui_MainWindow.flag == 0:
            self.ani = FuncAnimation(self.canvas.figure, self.update_line, frames=10, blit=True, interval=0)
            Ui_MainWindow.flag = 1

    def on_stop(self):
        if Ui_MainWindow.flag == 1:
            self.ani._stop()
            Ui_MainWindow.flag = 0

    def tableView_init(self, i):
        if i == 0:
            # 创建一个 0行2列 的标准模型
            self.model = QtGui.QStandardItemModel(0, 2)

            self.tableview = QtWidgets.QTableView(self.verticalLayoutWidget)
            self.tableview.setFont(self.SetFont())
            self.tableview.setObjectName("tableView")
            self.verticalLayout.addWidget(self.tableview)

            # 创建 tableView 组件
            # 将 tableView 添加到垂直盒布局里

            # tableView 组件 设置模型
            self.tableview.setModel(self.model)

            self.tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
            # self.tableview.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置只能选中整行
            self.tableview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 不可编辑
            self.tableview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            # 设置只能选中一行

            # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
            # self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行
        if i == 1:
            self.model2 = QtGui.QStandardItemModel(0, 2)
            self.model2.setHorizontalHeaderLabels(['parameter', 'value'])

            self.tableview2 = QtWidgets.QTableView(self.verticalLayoutWidget_2)
            self.tableview2.setFont(self.SetFont())
            self.tableview2.setObjectName("tableview2")
            self.verticalLayout_2.addWidget(self.tableview2)
            self.tableview2.setModel(self.model2)
            self.tableview2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
            self.tableview.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置只能选中整行
            self.tableview2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 不可编辑
            self.tableview2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

            # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
            # self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行

    def tableView_add(self, i):
        if i == 0:
            io.read('user')
            for i in range(2, 7):
                self.model.appendRow([
                    QtGui.QStandardItem(io.userdata.columns[i]),
                    QtGui.QStandardItem(f'{io.userdata.iloc[io.userid, i]}')
                ])
        if i == 1:

            self.parameter_list = ['Body weight[kg]', 'Flight T[s]',
                                   'Jump T[s]', 'Jump Height from Flight T[m]',
                                   'Start interval relative F[%BW] ', 'Relative maximal F[%BW] ',
                                   'Start interval A[m/s^2] ']
            self.value_list = [self.body_mass,
                               self.flight_T,
                               self.jump_T,
                               self.jump_height_from_flight_T,
                               self.Start_interval_relative_F,
                               self.relative_max_F,
                               self.start_interval_A]
            self.model2.appendRow([
                QtGui.QStandardItem(f'——————jump {parameter.count1}—————'),
                QtGui.QStandardItem('—————')
            ])
            parameter.count1 += 1
            for i in range(0, 7):
                self.model2.appendRow([
                    QtGui.QStandardItem(self.parameter_list[i]),
                    QtGui.QStandardItem(f'{round(self.value_list[i], 3)}')
                ])
            self.tableview2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def tableView_clear(self):

        self.model.clear()


class Ui_Edit1(object):
    def setupUi(self, Edit1):
        Edit1.setObjectName("Edit1")
        Edit1.resize(341, 221)
        self.centralwidget = QtWidgets.QWidget(Edit1)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 261, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineEdit.setFont(font)
        self.LineEdit.setObjectName("LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)

        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox)

        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(300)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 150, 261, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.Edit)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        Edit1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edit1)
        QtCore.QMetaObject.connectSlotsByName(Edit1)

    def retranslateUi(self, Edit1):
        _translate = QtCore.QCoreApplication.translate
        Edit1.setWindowTitle(_translate("Edit1", "Edit1"))
        self.label.setText(_translate("Edit1", "Name:"))
        self.label_2.setText(_translate("Edit1", "Gender:"))
        self.label_3.setText(_translate("Edit1", "Weight（kg）："))
        self.label_4.setText(_translate("Edit1", "Height（cm）:"))
        self.comboBox.setItemText(0, _translate("Edit1", "Male"))
        self.comboBox.setItemText(1, _translate("Edit1", "Female"))
        self.comboBox.setItemText(2, _translate("Edit1", "Other Gender"))
        self.pushButton.setText(_translate("Edit1", "Submit"))
        self.pushButton_2.setText(_translate("Edit1", "Cancel"))

    def Edit(self):
        name = self.LineEdit.text()
        gender = self.comboBox.currentText()
        weight = self.spinBox.text()
        height = self.spinBox_2.text()
        BMI = round(eval(weight) / (eval(height) ** 2 / 10000), 2)
        io.userdata.iloc[io.userid, 2:7] = [name, gender, weight, height, BMI]
        io.write('user')


class Ui_Password(object):
    def setupUi(self, Password):
        Password.setObjectName("Password")
        Password.resize(440, 150)
        self.centralwidget = QtWidgets.QWidget(Password)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 390, 160))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineEdit.setFont(font)
        self.LineEdit.setObjectName("LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineEdit_2.setFont(font)
        self.LineEdit_2.setObjectName("LineEdit2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 390, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText(" ")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 390, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.CheckPassword)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        Password.setCentralWidget(self.centralwidget)

        self.retranslateUi(Password)
        QtCore.QMetaObject.connectSlotsByName(Password)

    def retranslateUi(self, Password):
        _translate = QtCore.QCoreApplication.translate
        Password.setWindowTitle(_translate("Password", "Password"))
        self.label.setText(_translate("Password", "New Password: "))
        self.label_2.setText(_translate("Password", "Confirm Password:"))
        self.pushButton.setText(_translate("Password", "Submit"))
        self.pushButton_2.setText(_translate("Password", "Cancel"))

    def CheckPassword(self):
        password = self.LineEdit.text()
        confirm_password = self.LineEdit_2.text()
        if password != confirm_password:
            self.label_3.setText('Password and confirm password do not match.')

        elif len(password) < 6:
            self.label_3.setGeometry(QtCore.QRect(40, 80, 390, 20))
            self.label_3.setText('Password must be at least 6 characters. ')
        else:
            self.label_3.setGeometry(QtCore.QRect(120, 80, 390, 20))
            self.label_3.setText('Reset password success.')
            io.userdata.iloc[io.userid, 1] = password
            io.write('user')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Login = QtWidgets.QMainWindow()
    ui1 = Ui_Login()
    ui1.setupUi(Login)

    Register = QtWidgets.QMainWindow()


    def check():
        i = ui1.flag
        if i:
            Main.show()
            ui3.tableView_clear()
            ui3.tableView_add(0)


    def update():
        ui3.tableView_clear()
        ui3.tableView_add(0)


    ui2 = Ui_Register()
    ui2.setupUi(Register)

    Main = QtWidgets.QMainWindow()
    ui3 = Ui_MainWindow()
    ui3.setupUi(Main)

    Edit1 = QtWidgets.QMainWindow()
    ui4 = Ui_Edit1()
    ui4.setupUi(Edit1)

    Password = QtWidgets.QMainWindow()
    ui5 = Ui_Password()
    ui5.setupUi(Password)
    Login.show()

    ui1.Register.clicked.connect(Register.show)
    ui2.Quit.clicked.connect(Register.hide)
    ui1.SignIn.clicked.connect(check)
    ui3.EditButton.clicked.connect(Edit1.show)
    ui3.PasswordButton.clicked.connect(Password.show)
    ui4.pushButton_2.clicked.connect(Edit1.hide)
    ui4.pushButton.clicked.connect(update)
    ui5.pushButton_2.clicked.connect(Password.hide)

    sys.exit(app.exec_())
