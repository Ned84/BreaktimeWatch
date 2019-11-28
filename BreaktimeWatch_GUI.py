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
from BreaktimeWatch import Functions as btwf



class Ui_BreaktimeWatchGUI(object):
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
        self.minlabel = QtWidgets.QLabel(self.centralwidget)
        self.minlabel.setGeometry(QtCore.QRect(246, 256, 55, 16))
        self.minlabel.setObjectName("minlabel")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 392, 236))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(160, 253, 121, 23))
        self.progressBar.setMaximum(60)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
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
        self.minTextbox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.minTextbox.setGeometry(QtCore.QRect(50, 250, 104, 30))
        self.minTextbox.setReadOnly(True)
        self.minTextbox.setObjectName("minTextbox")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 230, 151, 111))
        self.frame.setStyleSheet("image: url(:/resources/background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.minspinBox.raise_()
        self.minTextbox.raise_()
        self.editButton1.raise_()
        self.totallabel.raise_()
        self.minlabel.raise_()
        self.calendarWidget.raise_()
        self.progressBar.raise_()
        self.startButton.raise_()
        self.stopButton.raise_()
        self.frame.raise_()
        BreaktimeWatchGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(BreaktimeWatchGUI)
        QtCore.QMetaObject.connectSlotsByName(BreaktimeWatchGUI)

        @pyqtSlot()
        def on_click():
            self.minTextbox.setPlainText("{0}".format(btwf.total))

        self.startButton.clicked.connect(btwf.Start)
        self.stopButton.clicked.connect(btwf.Stop)
        self.stopButton.clicked.connect(on_click)

        


    def retranslateUi(self, BreaktimeWatchGUI):
        _translate = QtCore.QCoreApplication.translate
        BreaktimeWatchGUI.setWindowTitle(_translate("BreaktimeWatchGUI", "BreaktimeWatch"))
        self.editButton1.setText(_translate("BreaktimeWatchGUI", "Edit"))
        self.totallabel.setText(_translate("BreaktimeWatchGUI", "<html><head/><body><p><span style=\" font-size:11pt;\">Total</span></p></body></html>"))
        self.minlabel.setText(_translate("BreaktimeWatchGUI", "0 min"))
        self.startButton.setText(_translate("BreaktimeWatchGUI", "Start"))
        self.stopButton.setText(_translate("BreaktimeWatchGUI", "Stop"))



import Resources_rc



import sys
app = QtWidgets.QApplication(sys.argv)
BreaktimeWatchGUI = QtWidgets.QMainWindow()
ui = Ui_BreaktimeWatchGUI()
ui.setupUi(BreaktimeWatchGUI)
BreaktimeWatchGUI.show()
sys.exit(app.exec_())
