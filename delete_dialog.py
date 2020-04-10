# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class Ui_delete_dialog(QtWidgets.QDialog):
    delete_signal = pyqtSignal(dict)

    def emit(self):
        lineedit_content = self.lineEdit.text()
        content = {'lineedit_content':lineedit_content}
        self.delete_signal.emit(content)

    def setupUi(self, delete_dialog):
        delete_dialog.setObjectName("delete_dialog")
        delete_dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(delete_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(delete_dialog)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(delete_dialog)
        self.label.setGeometry(QtCore.QRect(80, 100, 72, 15))
        self.label.setObjectName("label")

        self.retranslateUi(delete_dialog)
        self.buttonBox.accepted.connect(delete_dialog.accept)
        self.buttonBox.rejected.connect(delete_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(delete_dialog)

        self.buttonBox.accepted.connect(self.emit)

    def retranslateUi(self, delete_dialog):
        _translate = QtCore.QCoreApplication.translate
        delete_dialog.setWindowTitle(_translate("delete_dialog", "Dialog"))
        self.label.setText(_translate("delete_dialog", "id:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_dialog = QtWidgets.QDialog()
    ui = Ui_delete_dialog()
    ui.setupUi(delete_dialog)
    delete_dialog.show()
    sys.exit(app.exec_())

