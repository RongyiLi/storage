from main_ui import *
from insert_dialog import *
from delete_dialog import *
from update_dialog import *
import sys
import pymysql


class Main(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.db = pymysql.connect(
            host="127.0.0.1",
            user='root',
            password='12345',
            database='storage',
        )

        self.cursor = self.db.cursor()
        self.textbrowser_value.setOpenExternalLinks(True)

        self.connect()

    def connect(self):
        self.button_select.clicked.connect(self.select)
        self.button_insert.clicked.connect(self.insert)
        self.button_update.clicked.connect(self.update)
        self.button_delete.clicked.connect(self.delete)
        self.action_insert.triggered.connect(self.insert)
        self.action_update.triggered.connect(self.update)
        self.action_delete.triggered.connect(self.delete)

    def select(self):
        lineedit_content = self.lineedit_key.text()
        if lineedit_content:
            if lineedit_content == 'all':
                sql = "select * from storage"
            else:
                sql = "select * from storage where k like '%{}%'".format(lineedit_content)
            # print(sql)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            self.textbrowser_value.clear()
            if results:
                template = "<a href='{}'>{}</a>"
                for row in results:
                    # print(row)
                    self.textbrowser_value.append(str(row[0]))
                    self.textbrowser_value.append(row[1])
                    # self.textbrowser_value.append(row[2])
                    for r in row[2].split('\n'):
                        if r.startswith('http'):
                            self.textbrowser_value.append(template.format(r,r))
                        else:
                            self.textbrowser_value.append(r)
            else:
                self.textbrowser_value.setText("未查询到 " + lineedit_content)

    def insert(self):
        def getInsertDialogSignal(content):
            if content['lineedit_content'] and content['textedit_content']:
                sql = "insert into storage(k,v) values('{}','{}')".format(content['lineedit_content'],
                                                                          content['textedit_content'])
                # print(sql)
                self.cursor.execute(sql)
                self.db.commit()

        insert_dialog = QtWidgets.QDialog()
        ui = Ui_insert_dialog()
        ui.setupUi(insert_dialog)
        ui.insert_signal.connect(getInsertDialogSignal)
        insert_dialog.show()
        insert_dialog.exec_()

    def update(self):
        def getUpdateDialogSignal(content):
            if content['lineedit_content'] and content['textedit_content'] and content['textedit_content']:
                sql = "update storage set k='{}',v='{}' where id={}".format(content['lineedit_content'],
                                                                            content['textedit_content'],
                                                                            content['id'])
                # print(sql)
                self.cursor.execute(sql)
                self.db.commit()

        def search(content):
            if content['id']:
                sql = "select * from storage where id={}".format(content['id'])
                # print(sql)
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                if results:
                    ui.lineEdit_key.setText(results[0][1])
                    ui.textEdit_value.setText(results[0][2])

        update_dialog = QtWidgets.QDialog()
        ui = Ui_update_dialog()
        ui.setupUi(update_dialog)
        ui.update_signal.connect(getUpdateDialogSignal)
        ui.id_signal.connect(search)
        update_dialog.show()
        update_dialog.exec_()

    def delete(self):
        def getDeleteDialogSignal(content):
            if content['lineedit_content']:
                sql = "delete from storage where id={}".format(content['lineedit_content'])
                # print(sql)
                self.cursor.execute(sql)
                self.db.commit()

        delete_dialog = QtWidgets.QDialog()
        ui = Ui_delete_dialog()
        ui.setupUi(delete_dialog)
        ui.delete_signal.connect(getDeleteDialogSignal)
        delete_dialog.show()
        delete_dialog.exec_()

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
