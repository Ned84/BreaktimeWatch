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
from urllib import request

import BreaktimeWatch as btwf

import os.path
from os import path
from datetime import datetime
import json
import math
import webbrowser

version = "1.2"

class Ui_BreaktimeWatchGUI(object):

    updateavail = False
    serverconnection = False
    versionnew = ""
    updatecnt = 0

    def __init__(self, *args, **kwargs):
        try:
            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch')

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta')

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam')

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\logfiles') == False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\logfiles')
           

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.json') == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\tmedta\\Data.json',"w+")
                data = [{"date": "November 01, 1984","totaltime": 6013}]
                json.dump(data,file, indent=1, sort_keys=True)
                file.close()

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam\\Param.json') == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\btwtwparam\\Param.json',"w+")
                data = [{"version": version,   "workhours/week": "",   "unpaid_breaktime": "",   "time_bfr_break": ""}]
                json.dump(data,file, indent=1, sort_keys=True)
                file.close()

            if path.exists(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\logfiles\\btwlog.txt') == False:
                file = open(os.getenv('LOCALAPPDATA') + '\\BreaktimeWatch\\logfiles\\btwlog.txt',"w+")
                file.close()

            daynow = datetime.now().strftime("%d-%m, %Y")
            btwf.Functions.GetTotalFromJson(daynow)
            btwf.Functions.totalmin = btwf.Functions.totalsec / 60
            btwf.Functions.totalmin = math.floor(btwf.Functions.totalmin)

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
        BreaktimeWatchGUI.resize(425, 420)
        BreaktimeWatchGUI.setMinimumSize(QtCore.QSize(425, 420))
        BreaktimeWatchGUI.setMaximumSize(QtCore.QSize(425, 420))
        BreaktimeWatchGUI.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/BtWbgr_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BreaktimeWatchGUI.setWindowIcon(icon)
        BreaktimeWatchGUI.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(BreaktimeWatchGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(False)
        self.calendarWidget.setGeometry(QtCore.QRect(15, 10, 392, 236))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget.setGridVisible(False)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 250, 425, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 212px; background-color: rgb(85, 255, 127); font: 10pt Arial}")    
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.calendarWidget.setObjectName("calendarWidget")
        self.startButton = QtWidgets.QPushButton(self.tab)
        self.startButton.setGeometry(QtCore.QRect(10, 55, 93, 28))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.tab)
        self.stopButton.setGeometry(QtCore.QRect(110, 55, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setEnabled(False)
        self.editButton1 = QtWidgets.QPushButton(self.tab)
        self.editButton1.setGeometry(QtCore.QRect(210, 55, 93, 28))
        self.editButton1.setObjectName("editButton1")
        self.minTextbox = QtWidgets.QPlainTextEdit(self.tab)
        self.minTextbox.setGeometry(QtCore.QRect(160, 19, 104, 30))
        self.minTextbox.setReadOnly(True)
        self.minTextbox.setObjectName("minTextbox")
        self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
        self.minTextbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minTextbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minTextbox.setFont(QtGui.QFont("Arial", 11))
        self.minTextbox.hide()
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(165, 19, 104, 30))
        self.label.setObjectName("minTextLabel")
        self.label.setText("{0}".format(btwf.Functions.totalmin))
        self.label.setFont(QtGui.QFont("Arial", 11))
        self.label.setText("{0}".format(btwf.Functions.totalmin))
        self.totallabel = QtWidgets.QLabel(self.tab)
        self.totallabel.setEnabled(True)
        self.totallabel.setGeometry(QtCore.QRect(115, 24, 44, 21))
        self.totallabel.setObjectName("totallabel")
        self.totallabel.setFont(QtGui.QFont("Arial", 11))
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(290, -5, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/BtWbgre.png);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(270, 19, 30, 30))
        self.frame_2.setStyleSheet("image: url(:/resources/stopwatch.svg);")
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.hide()       
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(290, -10, 151, 111))
        self.frame_3.setStyleSheet("image: url(:/resources/WorktimeWatch_Logo);")
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.minTextbox.raise_()
        self.label.raise_()
        self.editButton1.raise_()
        self.totallabel.raise_()
        self.calendarWidget.raise_()
        self.startButton.raise_()
        self.stopButton.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        BreaktimeWatchGUI.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(BreaktimeWatchGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 411, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        BreaktimeWatchGUI.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(BreaktimeWatchGUI)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdate = QtWidgets.QAction(BreaktimeWatchGUI)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionSettings = QtWidgets.QAction(BreaktimeWatchGUI)
        self.actionSettings.setObjectName("actionSettings")
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)      
        self.menuEdit.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(BreaktimeWatchGUI)
        QtCore.QMetaObject.connectSlotsByName(BreaktimeWatchGUI)

        @pyqtSlot()
        def WriteMinInTextbox():
            self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
            self.label.setText("{0}".format(btwf.Functions.totalmin))

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
            btwf.Functions.GetTotalFromJson(daychosen)
            self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
            self.label.setText("{0}".format(btwf.Functions.totalmin))

        @pyqtSlot()
        def EditOnOff():         
            if self.minTextbox.isReadOnly() == False:
                self.minTextbox.hide()
                self.label.show()
                self.minTextbox.setReadOnly(True)
                self.calendarWidget.setEnabled(False)
                self.calendarWidget.setSelectedDate(datetime.now())
                daychosen = self.calendarWidget.selectedDate().toString("dd-MM, yyyy")
                btwf.Functions.GetTotalFromJson(daychosen)
                btwf.Functions.totalmin = btwf.Functions.totalsec / 60
                btwf.Functions.totalmin = math.floor(btwf.Functions.totalmin)
                self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
                self.label.setText("{0}".format(btwf.Functions.totalmin))
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
                btwf.Functions.WriteTimeToJson(daychosen,timechosen)
            else:
                btwf.Functions.GetTotalFromJson(daychosen)
                btwf.Functions.totalmin = btwf.Functions.totalsec / 60
                btwf.Functions.totalmin = math.floor(btwf.Functions.totalmin)
                self.minTextbox.setPlainText("{0}".format(btwf.Functions.totalmin))
                self.label.setText("{0}".format(btwf.Functions.totalmin))

        @pyqtSlot()
        def OpenDialogAbout(): 
            self.window = QtWidgets.QDialog()
            self.ui = Ui_DialogAbout()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def OpenDialogUpdate(): 
            self.window = QtWidgets.QDialog()
            self.ui = Ui_DialogUpdate()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def OpenDialogSettings(): 
            self.window = QtWidgets.QDialog()
            self.ui = Ui_DialogSettings()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def StartButtonPressed():
            if Ui_BreaktimeWatchGUI.updateavail == False or Ui_BreaktimeWatchGUI.updatecnt == 1:
                btwf.Functions.Start(self)
                ShowWatch()
        
            if Ui_BreaktimeWatchGUI.updateavail == True and Ui_BreaktimeWatchGUI.updatecnt == 0:
               OpenDialogUpdate()
               Ui_BreaktimeWatchGUI.updatecnt = 1

        
        self.startButton.clicked.connect(StartButtonPressed)

        self.stopButton.clicked.connect(btwf.Functions.Stop)
        self.stopButton.clicked.connect(WriteMinInTextbox)
        self.stopButton.clicked.connect(DisableWatch)

        self.editButton1.clicked.connect(EditOnOff)

        self.calendarWidget.clicked.connect(ChangeSelectedDate)

        self.minTextbox.blockCountChanged.connect(EditTimeValue)

        self.actionAbout.triggered.connect(OpenDialogAbout)

        self.actionUpdate.triggered.connect(OpenDialogUpdate)

        self.actionSettings.triggered.connect(OpenDialogSettings)


    def retranslateUi(self, BreaktimeWatchGUI):
        _translate = QtCore.QCoreApplication.translate
        BreaktimeWatchGUI.setWindowTitle(_translate("BreaktimeWatchGUI", "BreaktimeWatch"))
        self.editButton1.setText(_translate("BreaktimeWatchGUI", "Edit"))
        self.totallabel.setText(_translate("BreaktimeWatchGUI", "<html><head/><body><p><span style=\" font-size:11pt;\">Total</span></p></body></html>"))
        self.startButton.setText(_translate("BreaktimeWatchGUI", "Start"))
        self.stopButton.setText(_translate("BreaktimeWatchGUI", "Stop"))
        self.menuEdit.setTitle(_translate("BreaktimeWatchGUI", "Edit"))
        self.menuHelp.setTitle(_translate("BreaktimeWatchGUI", "Help"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BreaktimeWatchGUI", "Breaktimewatch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BreaktimeWatchGUI", "WorktimeWatch"))
        self.actionAbout.setText(_translate("BreaktimeWatchGUI", "About"))
        self.actionUpdate.setText(_translate("BreaktimeWatchGUI", "Update"))
        self.actionSettings.setText(_translate("BreaktimeWatchGUI", "Settings"))

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName("DialogAbout")
        DialogAbout.resize(459, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAbout.setWindowIcon(icon)
        DialogAbout.setStyleSheet("")
        self.OKButton = QtWidgets.QPushButton(DialogAbout)
        self.OKButton.setGeometry(QtCore.QRect(350, 200, 93, 28))
        self.OKButton.setStyleSheet("")
        self.OKButton.setObjectName("OKButton")
        self.frame = QtWidgets.QFrame(DialogAbout)
        self.frame.setGeometry(QtCore.QRect(0, 50, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/BtWbgre.png);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(DialogAbout)
        self.label.setGeometry(QtCore.QRect(170, 60, 301, 131))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogAbout)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

        self.OKButton.clicked.connect(DialogAbout.close)

    def retranslateUi(self, DialogAbout):
        _translate = QtCore.QCoreApplication.translate
        DialogAbout.setWindowTitle(_translate("DialogAbout", "About"))
        self.OKButton.setText(_translate("DialogAbout", "Close"))
        self.label.setText(_translate("DialogAbout", "Version: "+ version +"\n"
"\n"
"Program to track breaktimes\n"
"(coffe- or smokebreak) during\n"
"workhours.\n"
"\n"
"Copyright (C) 2019  Ned84\n"
"ned84@protonmail.com"))
        self.label_2.setText(_translate("DialogAbout", "BreaktimeWatch"))

class Ui_DialogUpdate(object):
    def setupUi(self, DialogUpdate):
        DialogUpdate.setObjectName("DialogUpdate")
        DialogUpdate.resize(459, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogUpdate.setWindowIcon(icon)
        DialogUpdate.setStyleSheet("")
        self.OKButton = QtWidgets.QPushButton(DialogUpdate)
        self.OKButton.setGeometry(QtCore.QRect(350, 200, 93, 28))
        self.OKButton.setStyleSheet("")
        self.OKButton.setObjectName("OKButton")
        self.UpdateButton = QtWidgets.QPushButton(DialogUpdate)
        self.UpdateButton.setGeometry(QtCore.QRect(250, 200, 93, 28))
        self.UpdateButton.setStyleSheet("")
        self.UpdateButton.setObjectName("UpdateButton")
        self.frame = QtWidgets.QFrame(DialogUpdate)
        self.frame.setGeometry(QtCore.QRect(0, 50, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/BtWbgre.png);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(DialogUpdate)
        self.label.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label_3 = QtWidgets.QLabel(DialogUpdate)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label_4 = QtWidgets.QLabel(DialogUpdate)
        self.label_4.setGeometry(QtCore.QRect(170, 60, 301, 131))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogUpdate)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogUpdate)
        QtCore.QMetaObject.connectSlotsByName(DialogUpdate)

        @pyqtSlot()
        def OpenUpdateSite():
            webbrowser.open('https://github.com/Ned84/BreaktimeWatch/releases') 

        self.OKButton.clicked.connect(DialogUpdate.close)

        self.UpdateButton.clicked.connect(OpenUpdateSite)

    def retranslateUi(self, DialogUpdate):
        _translate = QtCore.QCoreApplication.translate
        DialogUpdate.setWindowTitle(_translate("DialogUpdate", "Update BreaktimeWatch"))
        self.OKButton.setText(_translate("DialogUpdate", "Close"))
        self.UpdateButton.setText(_translate("DialogUpdate", "Update"))
        self.label.setText(_translate("DialogUpdate", "Current Version: "+ version +"\n"
"\n"
"New Version: "+ Ui_BreaktimeWatchGUI.versionnew +"\n"
"\n"
"Do you want to Update\n"
"this Program?"))

        self.label_3.setText(_translate("DialogUpdate", "No connection to Github."))
        self.label_3.setFont(QtGui.QFont("Arial", 9))

        self.label_4.setText(_translate("DialogUpdate", "Current Version: "+ version +"\n"
"\n"
"New Version: "+ Ui_BreaktimeWatchGUI.versionnew +"\n"
"\n"
"No Update available."))
        self.label_4.setFont(QtGui.QFont("Arial", 9))

        self.label.setFont(QtGui.QFont("Arial", 9))
        self.label_2.setText(_translate("DialogUpdate", "BreaktimeWatch"))

        if Ui_BreaktimeWatchGUI.serverconnection == False:
            self.UpdateButton.setEnabled(False)
            self.label.hide()
            self.label_4.hide()
            self.label_3.show()
        else:
            if Ui_BreaktimeWatchGUI.updateavail == True:
                self.UpdateButton.setEnabled(True)
                self.label.show()
                self.label_4.hide()
                self.label_3.hide()
            else:
                self.UpdateButton.setEnabled(False)
                self.label.hide()
                self.label_4.show()
                self.label_3.hide()

class Ui_DialogSettings(object):

    def setupUi(self, DialogSettings):
        DialogSettings.setObjectName("DialogSettings")
        DialogSettings.resize(459, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogSettings.setWindowIcon(icon)
        DialogSettings.setStyleSheet("")
        self.OKButton = QtWidgets.QPushButton(DialogSettings)
        self.OKButton.setGeometry(QtCore.QRect(250, 200, 93, 28))
        self.OKButton.setStyleSheet("")
        self.OKButton.setObjectName("OKButton")
        self.frame = QtWidgets.QFrame(DialogSettings)
        self.frame.setGeometry(QtCore.QRect(0, 50, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/WorktimeWatch_Logo.png);")
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(DialogSettings)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.CancelButton = QtWidgets.QPushButton(DialogSettings)
        self.CancelButton.setGeometry(QtCore.QRect(350, 200, 93, 28))
        self.CancelButton.setObjectName("CancelButton")
        self.label = QtWidgets.QLabel(DialogSettings)
        self.label.setGeometry(QtCore.QRect(160, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(DialogSettings)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogSettings)
        self.label_4.setGeometry(QtCore.QRect(160, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(DialogSettings)
        self.lineEdit.setGeometry(QtCore.QRect(330, 70, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(DialogSettings)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 100, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(DialogSettings)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 130, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(DialogSettings)
        self.CancelButton.clicked.connect(DialogSettings.close)
        QtCore.QMetaObject.connectSlotsByName(DialogSettings)

        try: 

            btwf.Functions.GetSettingsFromJson()
            self.lineEdit.setText(btwf.Functions.paramworkhoursweek)
            self.lineEdit_2.setText(btwf.Functions.paramunpaid_breaktime)
            self.lineEdit_3.setText(btwf.Functions.paramtime_bfr_break)
           
        except Exception as exc:
            btwf.Functions.WriteLog(exc)

    def retranslateUi(self, DialogSettings):
        _translate = QtCore.QCoreApplication.translate
        DialogSettings.setWindowTitle(_translate("DialogSettings", "About BreaktimeWatch"))
        self.OKButton.setText(_translate("DialogSettings", "OK"))
        self.label_2.setText(_translate("DialogSettings", "Settings"))
        self.CancelButton.setText(_translate("DialogSettings", "Cancel"))
        self.label.setText(_translate("DialogSettings", "Workhours/Week"))
        self.label_3.setText(_translate("DialogSettings", "Unpaid breaktime/day"))
        self.label_4.setText(_translate("DialogSettings", "Worktime before break"))        

        


import Resources_rc


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    BreaktimeWatchGUI = QtWidgets.QMainWindow()
    ui = Ui_BreaktimeWatchGUI()
    ui.setupUi(BreaktimeWatchGUI)
    BreaktimeWatchGUI.show()
    sys.exit(app.exec_())



