# -*- encoding:utf-8 -*-

import os
from ConfigParser import SafeConfigParser

appDataPath = os.path.join(os.environ['APPDATA'], 'ulogger')
if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception as err:
        appDataPath = os.getcwd()

tabs = []
tabs_obj = {}

config = SafeConfigParser()
config.read("config.ini")

refresh_speed = config.get("Settings", "refresh_speed")
default_font = config.get("Settings", "default_font")
default_font_size = config.get("Settings", "default_font_size")

appName = "TabbyLogger"
appVersion = "0.1"
pauseFlag = False
maxLines = -2000