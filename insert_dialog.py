# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal


class Ui_insert_dialog(QtWidgets.QDialog):
    insert_signal = pyqtSignal(dict)

    def emit(self):
        lineedit_content = self.lineEdit.text().strip()
        textedit_content = self.textEdit.toPlainText().strip()
        content = {'lineedit_content':lineedit_content,'textedit_content':textedit_content}
        self.insert_signal.emit(content)

    def setupUi(self, insert_dialog):
        insert_dialog.setObjectName("insert_dialog")
        insert_dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(insert_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(insert_dialog)
        self.textEdit.setGeometry(QtCore.QRect(33, 116, 341, 121))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(insert_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(32, 60, 341, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_key = QtWidgets.QLabel(insert_dialog)
        self.label_key.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label_key.setObjectName("label_key")
        self.label_value = QtWidgets.QLabel(insert_dialog)
        self.label_value.setGeometry(QtCore.QRect(30, 100, 72, 15))
        self.label_value.setObjectName("label_value")

        self.retranslateUi(insert_dialog)
        self.buttonBox.accepted.connect(insert_dialog.accept)
        self.buttonBox.rejected.connect(insert_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(insert_dialog)
        insert_dialog.setTabOrder(self.lineEdit, self.textEdit)

        self.buttonBox.accepted.connect(self.emit)

    def retranslateUi(self, insert_dialog):
        _translate = QtCore.QCoreApplication.translate
        insert_dialog.setWindowTitle(_translate("insert_dialog", "Dialog"))
        self.label_key.setText(_translate("insert_dialog", "key："))
        self.label_value.setText(_translate("insert_dialog", "values:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    insert_dialog = QtWidgets.QDialog()
    ui = Ui_insert_dialog()
    ui.setupUi(insert_dialog)
    insert_dialog.show()
    sys.exit(app.exec_())
