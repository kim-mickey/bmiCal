# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 423)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 100, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 100, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 100, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/Pictures/resources/apple.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(-4.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(32, 74, 135);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.weight = QtWidgets.QLabel(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.weight.setTextFormat(QtCore.Qt.AutoText)
        self.weight.setScaledContents(True)
        self.weight.setObjectName("weight")
        self.height = QtWidgets.QLabel(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.height.setTextFormat(QtCore.Qt.AutoText)
        self.height.setScaledContents(True)
        self.height.setObjectName("height")
        self.weight_ent = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_ent.setGeometry(QtCore.QRect(150, 30, 113, 25))
        self.weight_ent.setObjectName("weight_ent")
        self.height_ent = QtWidgets.QLineEdit(self.centralwidget)
        self.height_ent.setGeometry(QtCore.QRect(150, 70, 113, 25))
        self.height_ent.setObjectName("height_ent")
        self.kg = QtWidgets.QLabel(self.centralwidget)
        self.kg.setGeometry(QtCore.QRect(270, 30, 101, 21))
        self.kg.setTextFormat(QtCore.Qt.AutoText)
        self.kg.setScaledContents(True)
        self.kg.setObjectName("kg")
        self.cm = QtWidgets.QLabel(self.centralwidget)
        self.cm.setGeometry(QtCore.QRect(270, 70, 101, 21))
        self.cm.setTextFormat(QtCore.Qt.AutoText)
        self.cm.setScaledContents(True)
        self.cm.setObjectName("cm")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(180, 120, 89, 25))
        self.calculate.setObjectName("calculate")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 230, 161, 161))
        self.lcdNumber.setObjectName("lcdNumber")
        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.message.setTextFormat(QtCore.Qt.AutoText)
        self.message.setScaledContents(True)
        self.message.setObjectName("message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 547, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what this is shit</p><p><br/></p></body></html>"))
        self.weight.setText(_translate("MainWindow", "WEIGHT"))
        self.height.setText(_translate("MainWindow", "HEIGHT"))
        self.kg.setText(_translate("MainWindow", "kg"))
        self.cm.setText(_translate("MainWindow", "cm"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.message.setText(_translate("MainWindow", "Your BMI is:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
