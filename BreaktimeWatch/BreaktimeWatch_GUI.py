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

import BreaktimeWatch as btwf

import os.path
from os import path
from datetime import datetime
import json



class Ui_BreaktimeWatchGUI(object):

    def __init__(self, *args, **kwargs):
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

        return super().__init__(*args, **kwargs)
   


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
        self.totallabel.setGeometry(QtCore.QRect(5, 254, 44, 21))
        self.totallabel.setObjectName("totallabel")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(False)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 392, 236))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 290, 93, 28))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(110, 290, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.minspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.minspinBox.setEnabled(True)
        self.minspinBox.setGeometry(QtCore.QRect(50, 250, 104, 30))
        self.minspinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.minspinBox.setReadOnly(True)
        self.minspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.minspinBox.setObjectName("minspinBox")
        self.minspinBox.hide()
        self.minTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.minTextbox.setGeometry(QtCore.QRect(50, 250, 104, 30))
        self.minTextbox.setReadOnly(True)
        self.minTextbox.setObjectName("minTextbox")
        self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 230, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(160, 250, 30, 30))
        self.frame_2.setStyleSheet("image: url(:/resources/stopwatch.svg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.hide()
        self.minspinBox.raise_()
        self.minTextbox.raise_()
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
            self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))

        @pyqtSlot()
        def ProgressbarStart():     
            self.progressBar.setValue(btwf.Functions.completed)

        @pyqtSlot()
        def ShowWatch():     
            self.frame_2.show()

        @pyqtSlot()
        def DisableWatch(): 
            self.frame_2.hide()

        @pyqtSlot()
        def EditOnOff():         
            if self.minspinBox.isVisible() == True:
                self.minspinBox.hide()
                self.minTextbox.show()
                self.calendarWidget.setEnabled(False)
                self.calendarWidget.setSelectedDate(datetime.now())
            else:
                self.minspinBox.show()
                self.minTextbox.hide()
                self.calendarWidget.setEnabled(True)
          
                
        self.startButton.clicked.connect(btwf.Functions.Start)
        self.startButton.clicked.connect(ShowWatch)

        self.stopButton.clicked.connect(btwf.Functions.Stop)
        self.stopButton.clicked.connect(WriteMinInTextbox)
        self.stopButton.clicked.connect(DisableWatch)

        self.editButton1.clicked.connect(EditOnOff)





    def retranslateUi(self, BreaktimeWatchGUI):
        _translate = QtCore.QCoreApplication.translate
        BreaktimeWatchGUI.setWindowTitle(_translate("BreaktimeWatchGUI", "BreaktimeWatch"))
        self.editButton1.setText(_translate("BreaktimeWatchGUI", "Edit"))
        self.totallabel.setText(_translate("BreaktimeWatchGUI", "<html><head/><body><p><span style=\" font-size:11pt;\">Total</span></p></body></html>"))
        self.startButton.setText(_translate("BreaktimeWatchGUI", "Start"))
        self.stopButton.setText(_translate("BreaktimeWatchGUI", "Stop"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BreaktimeWatchGUI = QtWidgets.QMainWindow()
    ui = Ui_BreaktimeWatchGUI()
    ui.setupUi(BreaktimeWatchGUI)
    BreaktimeWatchGUI.show()
    sys.exit(app.exec_())
