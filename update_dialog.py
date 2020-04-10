# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class Ui_update_dialog(QtWidgets.QDialog):
    update_signal = pyqtSignal(dict)
    id_signal = pyqtSignal(dict)

    def emit(self):
        id = self.lineEdit_id.text()
        lineedit_content = self.lineEdit_key.text().strip()
        textedit_content = self.textEdit_value.toPlainText().strip()
        content = {'id': id, 'lineedit_content': lineedit_content, 'textedit_content': textedit_content}
        self. update_signal.emit(content)

    def search(self):
        id = self.lineEdit_id.text()
        content = {'id': id}
        self.id_signal.emit(content)


    def setupUi(self, update_dialog):
        update_dialog.setObjectName("update_dialog")
        update_dialog.resize(384, 285)
        self.buttonBox = QtWidgets.QDialogButtonBox(update_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_id = QtWidgets.QLineEdit(update_dialog)
        self.lineEdit_id.setGeometry(QtCore.QRect(60, 40, 113, 21))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_id.setValidator(QtGui.QIntValidator())
        self.lineEdit_key = QtWidgets.QLineEdit(update_dialog)
        self.lineEdit_key.setGeometry(QtCore.QRect(60, 90, 301, 21))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.textEdit_value = QtWidgets.QTextEdit(update_dialog)
        self.textEdit_value.setGeometry(QtCore.QRect(60, 140, 301, 87))
        self.textEdit_value.setObjectName("textEdit_value")
        self.button_search = QtWidgets.QPushButton(update_dialog)
        self.button_search.setGeometry(QtCore.QRect(200, 40, 93, 28))
        self.button_search.setObjectName("button_search")
        self.label_id = QtWidgets.QLabel(update_dialog)
        self.label_id.setGeometry(QtCore.QRect(60, 20, 72, 15))
        self.label_id.setObjectName("label_id")
        self.label_key = QtWidgets.QLabel(update_dialog)
        self.label_key.setGeometry(QtCore.QRect(60, 70, 72, 15))
        self.label_key.setObjectName("label_key")
        self.label_value = QtWidgets.QLabel(update_dialog)
        self.label_value.setGeometry(QtCore.QRect(60, 120, 72, 15))
        self.label_value.setObjectName("label_value")

        self.retranslateUi(update_dialog)
        self.buttonBox.accepted.connect(update_dialog.accept)
        self.buttonBox.rejected.connect(update_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(update_dialog)

        self.button_search.clicked.connect(self.search)
        self.buttonBox.accepted.connect(self.emit)

    def retranslateUi(self, update_dialog):
        _translate = QtCore.QCoreApplication.translate
        update_dialog.setWindowTitle(_translate("update_dialog", "Dialog"))
        self.button_search.setText(_translate("update_dialog", "搜索"))
        self.label_id.setText(_translate("update_dialog", "id:"))
        self.label_key.setText(_translate("update_dialog", "key:"))
        self.label_value.setText(_translate("update_dialog", "value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_dialog = QtWidgets.QDialog()
    ui = Ui_update_dialog()
    ui.setupUi(update_dialog)
    update_dialog.show()
    sys.exit(app.exec_())

