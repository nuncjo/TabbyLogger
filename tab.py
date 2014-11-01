# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab.ui'
#
# Created: Sat Nov 01 09:17:40 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 318)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.font_size_comboBox = QtGui.QComboBox(Form)
        self.font_size_comboBox.setObjectName("font_size_comboBox")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.font_size_comboBox.addItem("")
        self.gridLayout.addWidget(self.font_size_comboBox, 5, 4, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 5)
        self.fontComboBox = QtGui.QFontComboBox(Form)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout.addWidget(self.fontComboBox, 5, 3, 1, 1)
        self.scroll_checkBox = QtGui.QCheckBox(Form)
        self.scroll_checkBox.setObjectName("scroll_checkBox")
        self.gridLayout.addWidget(self.scroll_checkBox, 5, 5, 1, 1)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    selection-background-color: rgb(255, 0, 0);\n"
"}")
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 7)
        self.search_lineEdit = QtGui.QLineEdit(Form)
        self.search_lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.gridLayout.addWidget(self.search_lineEdit, 3, 0, 1, 1)
        self.clear_pushButton = QtGui.QPushButton(Form)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.gridLayout.addWidget(self.clear_pushButton, 5, 2, 1, 1)
        self.pause_pushButton = QtGui.QPushButton(Form)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.gridLayout.addWidget(self.pause_pushButton, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.clear_pushButton)
        Form.setTabOrder(self.clear_pushButton, self.fontComboBox)
        Form.setTabOrder(self.fontComboBox, self.font_size_comboBox)
        Form.setTabOrder(self.font_size_comboBox, self.scroll_checkBox)
        Form.setTabOrder(self.scroll_checkBox, self.lineEdit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(0, QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(1, QtGui.QApplication.translate("Form", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(2, QtGui.QApplication.translate("Form", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(3, QtGui.QApplication.translate("Form", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(4, QtGui.QApplication.translate("Form", "18", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(5, QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(6, QtGui.QApplication.translate("Form", "22", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(7, QtGui.QApplication.translate("Form", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(8, QtGui.QApplication.translate("Form", "26", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(9, QtGui.QApplication.translate("Form", "28", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(10, QtGui.QApplication.translate("Form", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(11, QtGui.QApplication.translate("Form", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(12, QtGui.QApplication.translate("Form", "34", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(13, QtGui.QApplication.translate("Form", "36", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(14, QtGui.QApplication.translate("Form", "38", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(15, QtGui.QApplication.translate("Form", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.font_size_comboBox.setItemText(16, QtGui.QApplication.translate("Form", "42", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Log path:", None, QtGui.QApplication.UnicodeUTF8))
        self.scroll_checkBox.setText(QtGui.QApplication.translate("Form", "Scroll down", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.search_lineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_pushButton.setText(QtGui.QApplication.translate("Form", "Clear Log File", None, QtGui.QApplication.UnicodeUTF8))
        self.pause_pushButton.setText(QtGui.QApplication.translate("Form", "Pause", None, QtGui.QApplication.UnicodeUTF8))

