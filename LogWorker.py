# -*- coding:utf-8 -*-

from PySide.QtCore import *

import time
import os
import config

class LogWorker(QThread):

    logRefreshSignal = Signal()

    def __init__(self, parent=None):
        super(LogWorker, self).__init__(parent)

        self._stop = False
        self._log_path = False

        self.interval = float(config.refresh_speed)
        self.current_file_size = 0

    def run(self):
        while True and not self._stop and self._log_path is not False:
            time.sleep(self.interval)
            if config.pauseFlag == False:
                actual_file_size = os.path.getsize(self._log_path)
                if actual_file_size > self.current_file_size:
                    self.current_file_size = actual_file_size
                    self.logRefreshSignal.emit()

    @property
    def log_path(self):
        return self._log_path

    @log_path.setter
    def log_path(self, value):
        self._log_path = value
        return self._log_path

    @log_path.deleter
    def log_path(self):
        del self._log_path

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value
        return self._stop

    @stop.deleter
    def stop(self):
        del self._stop