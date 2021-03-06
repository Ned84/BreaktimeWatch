# -*- coding: utf-8 -*-
"""
BreaktimeWatch | Program for tracking breaktimes (coffee- or smokebreak)
Copyright (C) 2019  Ned84 ned84@protonmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

import BreaktimeWatch_test as btwf

import os.path
from os import path
from datetime import datetime
import json
import math

version = "1.2"

class Ui_BreaktimeWatchGUI(object):

    def __init__(self, *args, **kwargs):
        try:
            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch')

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData')

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles')
           
            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.json') == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\TimeData\\Data.json',"w+")
                data = [{"date": "November 01, 1984","totaltime": 6013}]
                json.dump(data,file, indent=1, sort_keys=True)
                file.close()

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles\\btwlog.txt') == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\Logfiles\\btwlog.txt',"w+")
                file.close()

            daynow = datetime.now().strftime("%d-%m, %Y")
            btwf.TestFunctions.test_GetTotalFromJson(daynow)
            btwf.TestFunctions.totalmin = btwf.TestFunctions.totalsec / 60
            btwf.TestFunctions.totalmin = math.floor(btwf.TestFunctions.totalmin)

        except Exception as exc:
            Functions.WriteLog(exc)

        try:
            link = "https://github.com/Ned84/BreaktimeWatch/blob/master/Version.md"
  
            url = request.urlopen(link)
            readurl = url.read()
            text = readurl.decode(encoding='utf-8',errors='ignore')
            stringindex = text.find("BreaktimeWatchVersion") 

            if stringindex != -1:
                Ui_BreaktimeWatchGUI.versionnew = text[stringindex + 23:stringindex + 26]
                Ui_BreaktimeWatchGUI.versionnew = Ui_BreaktimeWatchGUI.versionnew.replace('_','.')

            if version != Ui_BreaktimeWatchGUI.versionnew:
                Ui_BreaktimeWatchGUI.serverconnection = True
                Ui_BreaktimeWatchGUI.updateavail = True
            else:
                Ui_BreaktimeWatchGUI.serverconnection = True
                Ui_BreaktimeWatchGUI.updateavail = False

            return super().__init__(*args, **kwargs)

        except Exception as exc: 
             Ui_BreaktimeWatchGUI.updateavail = False

   


    def setupUi(self, BreaktimeWatchGUI):
        BreaktimeWatchGUI.setObjectName("BreaktimeWatchGUI")
        BreaktimeWatchGUI.resize(411, 330)
        BreaktimeWatchGUI.setMinimumSize(QtCore.QSize(411, 330))
        BreaktimeWatchGUI.setMaximumSize(QtCore.QSize(411, 330))
        BreaktimeWatchGUI.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/background.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BreaktimeWatchGUI.setWindowIcon(icon)
        BreaktimeWatchGUI.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(BreaktimeWatchGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.editButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.editButton1.setGeometry(QtCore.QRect(210, 290, 93, 28))
        self.editButton1.setObjectName("editButton1")
        self.totallabel = QtWidgets.QLabel(self.centralwidget)
        self.totallabel.setEnabled(True)
        self.totallabel.setGeometry(QtCore.QRect(115, 259, 44, 21))
        self.totallabel.setObjectName("totallabel")
        self.totallabel.setFont(QtGui.QFont("Arial", 11))
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(False)
        self.calendarWidget.setGeometry(QtCore.QRect(15, 10, 392, 236))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 290, 93, 28))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(110, 290, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setEnabled(False)
        self.minTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.minTextbox.setGeometry(QtCore.QRect(160, 254, 104, 30))
        self.minTextbox.setReadOnly(True)
        self.minTextbox.setObjectName("minTextbox")
        self.minTextbox.setPlainText("{0}".format(btwf.TestFunctions.totalmin))
        self.minTextbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minTextbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minTextbox.setFont(QtGui.QFont("Arial", 11))
        self.minTextbox.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 254, 104, 30))
        self.label.setObjectName("minTextLabel")
        self.label.setText("{0}".format(btwf.TestFunctions.totalmin))
        self.label.setFont(QtGui.QFont("Arial", 11))
        self.label.setText("{0}".format(btwf.TestFunctions.totalmin))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 230, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/background.png);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(270, 255, 30, 30))
        self.frame_2.setStyleSheet("image: url(:/resources/stopwatch.svg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.hide()
        self.minTextbox.raise_()
        self.label.raise_()
        self.editButton1.raise_()
        self.totallabel.raise_()
        self.calendarWidget.raise_()
        self.startButton.raise_()
        self.stopButton.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        BreaktimeWatchGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(BreaktimeWatchGUI)
        QtCore.QMetaObject.connectSlotsByName(BreaktimeWatchGUI)

        @pyqtSlot()
        def WriteMinInTextbox():
            self.minTextbox.setPlainText("{0}".format(btwf.TestFunctions.totalmin))
            self.label.setText("{0}".format(btwf.TestFunctions.totalmin))

        @pyqtSlot()
        def ShowWatch():     
            self.frame_2.show()
            self.editButton1.setEnabled(False)
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)

        @pyqtSlot()
        def DisableWatch(): 
            self.frame_2.hide()
            self.editButton1.setEnabled(True)
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)

        @pyqtSlot()
        def ChangeSelectedDate(): 
            daychosen = self.calendarWidget.selectedDate().toString("dd-MM, yyyy")
            btwf.TestFunctions.test_GetTotalFromJson(daychosen)
            self.minTextbox.setPlainText("{0}".format(btwf.TestFunctions.totalmin))
            self.label.setText("{0}".format(btwf.TestFunctions.totalmin))

        @pyqtSlot()
        def EditOnOff():         
            if self.minTextbox.isReadOnly() == False:
                self.minTextbox.hide()
                self.label.show()
                self.minTextbox.setReadOnly(True)
                self.calendarWidget.setEnabled(False)
                self.calendarWidget.setSelectedDate(datetime.now())
                daychosen = self.calendarWidget.selectedDate().toString("dd-MM, yyyy")
                btwf.TestFunctions.test_GetTotalFromJson(daychosen)
                btwf.TestFunctions.totalmin = btwf.TestFunctions.totalsec / 60
                btwf.TestFunctions.totalmin = math.floor(btwf.TestFunctions.totalmin)
                self.minTextbox.setPlainText("{0}".format(btwf.TestFunctions.totalmin))
                self.label.setText("{0}".format(btwf.TestFunctions.totalmin))
                self.startButton.setEnabled(True)
                self.stopButton.setEnabled(False)
            else:
                self.minTextbox.show()
                self.label.hide()
                self.minTextbox.setReadOnly(False)
                self.calendarWidget.setEnabled(True)
                self.startButton.setEnabled(False)
                self.stopButton.setEnabled(False)

        @pyqtSlot()
        def EditTimeValue(): 
            daychosen = self.calendarWidget.selectedDate().toString("dd-MM, yyyy")
            
            timechosenstring = ("{0}".format(self.minTextbox.toPlainText()))
            timechosenstring = timechosenstring.rstrip()
            if timechosenstring.isdigit() :
                timechosen = int("{0}".format(self.minTextbox.toPlainText()))
                self.minTextbox.setPlainText("{0}".format(timechosen))
                self.label.setText("{0}".format(timechosen))
                timechosen = timechosen * 60
                btwf.TestFunctions.WriteTimeToJson(self, daychosen,timechosen)
            else:
                btwf.TestFunctions.test_GetTotalFromJson(daychosen)
                btwf.TestFunctions.totalmin = btwf.TestFunctions.totalsec / 60
                btwf.TestFunctions.totalmin = math.floor(btwf.TestFunctions.totalmin)
                self.minTextbox.setPlainText("{0}".format(btwf.TestFunctions.totalmin))
                self.label.setText("{0}".format(btwf.TestFunctions.totalmin))

        @pyqtSlot()
        def OpenDialog(): 
            self.window = QtWidgets.QDialog()
            self.ui = Ui_DialogAbout()
            self.ui.setupUi(self.window)
            self.window.show()
          
            
        self.startButton.clicked.connect(btwf.TestFunctions.test_Start)
        self.startButton.clicked.connect(ShowWatch)

        self.stopButton.clicked.connect(btwf.TestFunctions.test_Stop)
        self.stopButton.clicked.connect(WriteMinInTextbox)
        self.stopButton.clicked.connect(DisableWatch)

        self.editButton1.clicked.connect(EditOnOff)

        self.calendarWidget.clicked.connect(ChangeSelectedDate)

        self.minTextbox.blockCountChanged.connect(EditTimeValue)




    def retranslateUi(self, BreaktimeWatchGUI):
        _translate = QtCore.QCoreApplication.translate
        BreaktimeWatchGUI.setWindowTitle(_translate("BreaktimeWatchGUI", "BreaktimeWatch"))
        self.editButton1.setText(_translate("BreaktimeWatchGUI", "Edit"))
        self.totallabel.setText(_translate("BreaktimeWatchGUI", "<html><head/><body><p><span style=\" font-size:11pt;\">Total</span></p></body></html>"))
        self.startButton.setText(_translate("BreaktimeWatchGUI", "Start"))
        self.stopButton.setText(_translate("BreaktimeWatchGUI", "Stop"))
import Resources_rc_test


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    BreaktimeWatchGUI = QtWidgets.QMainWindow()
    ui = Ui_BreaktimeWatchGUI()
    ui.setupUi(BreaktimeWatchGUI)
    BreaktimeWatchGUI.show()
    sys.exit(app.exec_())
