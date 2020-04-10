# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textbrowser_value = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbrowser_value.setGeometry(QtCore.QRect(60, 140, 541, 381))
        self.textbrowser_value.setObjectName("textbrowser_value")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 10, 141, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_select.setObjectName("button_select")
        self.verticalLayout.addWidget(self.button_select)
        self.button_insert = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_insert.setObjectName("button_insert")
        self.verticalLayout.addWidget(self.button_insert)
        self.button_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_update.setObjectName("button_update")
        self.verticalLayout.addWidget(self.button_update)
        self.button_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout.addWidget(self.button_delete)
        self.lineedit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_key.setGeometry(QtCore.QRect(60, 80, 541, 31))
        self.lineedit_key.setObjectName("lineedit_key")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_insert = QtWidgets.QAction(MainWindow)
        self.action_insert.setObjectName("action_insert")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_delete = QtWidgets.QAction(MainWindow)
        self.action_delete.setObjectName("action_delete")
        self.menu.addAction(self.action_insert)
        self.menu.addAction(self.action_update)
        self.menu.addAction(self.action_delete)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineedit_key, self.textbrowser_value)
        MainWindow.setTabOrder(self.textbrowser_value, self.button_select)
        MainWindow.setTabOrder(self.button_select, self.button_insert)
        MainWindow.setTabOrder(self.button_insert, self.button_update)
        MainWindow.setTabOrder(self.button_update, self.button_delete)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_select.setText(_translate("MainWindow", "搜索"))
        self.button_insert.setText(_translate("MainWindow", "添加"))
        self.button_update.setText(_translate("MainWindow", "更新"))
        self.button_delete.setText(_translate("MainWindow", "删除"))
        self.menu.setTitle(_translate("MainWindow", "功能"))
        self.action_insert.setText(_translate("MainWindow", "添加"))
        self.action_update.setText(_translate("MainWindow", "更新"))
        self.action_delete.setText(_translate("MainWindow", "删除"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

