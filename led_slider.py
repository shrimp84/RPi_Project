# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led_slider.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
'''user code'''
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = LED(23)

led_pin=24
GPIO.setup(led_pin,GPIO.OUT)
pwm=GPIO.PWM(led_pin, 100)
pwm.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()
'''user code'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 110, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        
        '''user code'''
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        '''user code'''
        
        self.verticalSlider.setGeometry(QtCore.QRect(40, 60, 81, 231))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "LED Toggle"))
        '''user code'''
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)
        
    def sliderMov(self):
        value = self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        '''user code'''
        
'''user code'''
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''user code'''


