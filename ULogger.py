# -*- coding:utf-8 -*-

"""
Ulogger
~~~~~~~~~~~~
Simple log viewer with remembering open tabs.

Dependencies:
PySide 1.2.2 : http://qt-project.org/wiki/PySide
Pyhk : https://github.com/schurpf/pyhk

:copyright: (c) 2014 zoreander@gmail.com
"""

import math
import sys
import os
import cPickle
import pyhk

from PySide.QtGui import *
from PySide.QtCore import *

import gui
import tab
import config
import LogWorker

import atexit
import tempfile

sys.stdout = tempfile.TemporaryFile()
sys.stderr = tempfile.TemporaryFile()

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout.encoding

maxLines = math.fabs(config.maxLines)

class Tab(tab.Ui_Form, QWidget):


    def __init__(self, file,  parent=None):

        super(Tab, self).__init__(parent)
        self.setupUi(self)

        self.file = file
        self.next_flag = False
        self.sb = self.textEdit.verticalScrollBar()

        self.worker = LogWorker.LogWorker()
        self.worker.log_path = file
        self.worker.start()

        self.textEdit.setReadOnly(True)
        style = "QTextEdit {font-family:%s; font-size:%spx; selection-color:black; selection-background-color:yellow;}" % (config.default_font, config.default_font_size)
        self.textEdit.setStyleSheet(style)
        self.lineEdit.setReadOnly(True)
        self.scroll_checkBox.setChecked(True)
        self.lineEdit.setText(self.file)
        self.lineEdit.setReadOnly(True)

        #Signals
        self.clear_pushButton.clicked.connect(self.clear)
        self.search_lineEdit.returnPressed.connect(self.search)
        self.pause_pushButton.clicked.connect(self.pause)
        self.worker.logRefreshSignal.connect(self.refresh_log)
        self.fontComboBox.currentFontChanged.connect(self.set_font_style)
        self.font_size_comboBox.currentIndexChanged.connect(self.set_font_style)
        self.search_lineEdit.textChanged.connect(self.search_phrase_changed)


    def search_phrase_changed(self):
        self.next_flag = False

    def search(self):
        phrase = str(self.search_lineEdit.text())
        if not self.next_flag:
            self.textEdit.moveCursor(QTextCursor.Start)

        found = self.textEdit.find(phrase)
        if found:
            self.next_flag = True
        else:
            QMessageBox.information(self, "Information", "Search result not found")

    def closeEvent(self, event):
        try:
            self.worker.stop = True
        except ValueError as err:
            print err

    def set_font_style(self):
        family = self.fontComboBox.currentFont().family()
        size = int(self.font_size_comboBox.itemText(self.font_size_comboBox.currentIndex()))
        style = "QTextEdit {font-family:%s; font-size:%spx}" % (family, size)
        self.textEdit.setStyleSheet(style)

    def pause(self):
        if self.pause_pushButton.text() == 'Pause':
            config.pauseFlag = True
            self.pause_pushButton.setText('Resume')
        else:
            config.pauseFlag = False
            self.pause_pushButton.setText('Pause')

    def clear(self):
        try:
            with open(self.file, 'w') as f:
                f.write('')
            self.textEdit.clear()
            self.worker.current_file_size = 0
        except Exception as err:
            QMessageBox.critical(self, 'Error', 'Failed to clear log.')

    def load_log(self):
        try:
            with open(self.file, 'r') as f:

                lines = f.readlines()
                lines_count = len(lines)
                if lines_count > maxLines:
                    for line in lines[config.maxLines:lines_count]:
                        self.textEdit.insertPlainText(line)
                else:
                    for line in lines:
                        self.textEdit.insertPlainText(line)

        except Exception as err:
            QMessageBox.critical(self, 'Error', 'Failed to load log file.')

    def refresh_log(self):
        '''
        TODO: Optimization
        '''
        lines = []
        try:
            with open(self.file, 'r') as f:
                self.textEdit.clear()
                lines = f.readlines()
                lines_count = len(lines)
                if lines_count > maxLines:
                    for line in lines[config.maxLines:lines_count]:
                        self.textEdit.insertPlainText(line)
                else:
                    for line in lines:
                        self.textEdit.insertPlainText(line)

            if self.scroll_checkBox.isChecked():
                self.sb.setValue(self.sb.maximum())

        except Exception as err:
            QMessageBox.critical(self, 'Error', 'Failed to load log file.')

class MainWindow(gui.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        hot = pyhk.pyhk()
        self.shortcuts = 'CTRL+1:hide CTRL+2:normal CTRL+3:maximized CTRL+T:stays on top(default) CTRL+B:bottom CTRL+N:normal'
        hot.addHotkey(['Ctrl', '1'], self.hide)
        hot.addHotkey(['Ctrl', '2'], self.showNormal)
        hot.addHotkey(['Ctrl', '3'], self.showMaximized)
        hot.addHotkey(['Ctrl', 'T'], self.change_on_top)
        hot.addHotkey(['Ctrl', 'B'], self.change_on_bottom)
        hot.addHotkey(['Ctrl', 'N'], self.change_on_normal)

        self.setupUi(self)

        self.setWindowTitle("{} - {}".format(config.appName, config.appVersion))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.open_pushButton.clicked.connect(self.open_log)
        self.close_pushButton.clicked.connect(self.close_log)

        self.create_actions()
        self.create_tray_icon()
        self.open_logs()

    def change_on_normal(self):
        self.setWindowFlags(Qt.Window)
        self.showMessage(config.appName, unicode("Logger will behave normal"), 1000)
        self.show()

    def change_on_bottom(self):
        self.setWindowFlags(Qt.WindowStaysOnBottomHint)
        self.showMessage(config.appName, unicode("Logger will stay on bottom"), 1000)
        self.show()

    def change_on_top(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.showMessage(config.appName, unicode("Logger will stay on top"), 1000)
        self.show()

    def open_logs(self):
        if os.path.exists(os.path.join(config.appDataPath, 'tabs.ini')):
            try:
                config.tabs = cPickle.load(open(os.path.join(config.appDataPath, 'tabs.ini'), 'r'))
            except EOFError:
                config.tabs = []
            config.tabs = sorted(config.tabs)
            for t in config.tabs:
                tab = Tab(unicode(t))
                self.tabWidget.addTab(tab, os.path.basename(t))
                config.tabs_obj.update({self.tabWidget.count(): tab})

    def open_log(self):
        try:
            fd = QFileDialog.getOpenFileName(self, 'Open log file')
            if fd[0] != '':
                if fd[0] not in config.tabs:
                    tab = Tab(unicode(fd[0]))
                    self.tabWidget.addTab(tab, os.path.basename(fd[0]))
                    config.tabs.insert(0, fd[0])
                    config.tabs_obj.update({self.tabWidget.count(): tab})
                else:
                    QMessageBox.information(self, "Redundant Tab", "Log already opened in tabs.")

        except Exception as err:
             QMessageBox.critical(self, 'Error', 'Failed to load log file.')


    def close_log(self):

        if self.tabWidget.count() > 0:
            config.tabs.remove(self.tabWidget.currentWidget().lineEdit.text())
            self.tabWidget.currentWidget().close()
            self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def showEvent(self, event):
        self.statusBar().showMessage(self.shortcuts)

    def hideEvent(self, event):
        ''' Override hideEvent '''
        self.hide()
        self.trayIcon.show()
        self.showMessage(config.appName, unicode('Works in tray'), 1000)
        event.ignore()

    def closeEvent(self, event):
        with open(os.path.join(config.appDataPath, 'tabs.ini'), 'w') as f:
            cPickle.dump(config.tabs, f)

        for tab in config.tabs_obj.values():
            tab.worker.stop = True
            tab.worker.terminate()
            tab.close()

    def create_actions(self):
        self.restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        self.quitAction = QAction("&Quit", self, triggered=qApp.quit)

    def create_tray_icon(self):

        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon('img/icon2.png'))
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def showMessage(self, title, message, duration):
        icon = QSystemTrayIcon.MessageIcon()
        self.trayIcon.showMessage(title, message, icon, duration)


if __name__ == "__main__":

    QCoreApplication.setApplicationName(config.appName)
    QCoreApplication.setApplicationVersion(config.appVersion)
    QCoreApplication.setOrganizationName("Nuncjo")
    QCoreApplication.setOrganizationDomain("https://github.com/nuncjo")

    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec_())