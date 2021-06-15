# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymem
import re

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(683, 335)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(56, 58, 89);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 40, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 100, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.RADAR = QtWidgets.QPushButton(self.dropShadowFrame)
        self.RADAR.setGeometry(QtCore.QRect(240, 140, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.RADAR.setFont(font)
        self.RADAR.setStyleSheet(".QPushButton{\n"
"background-color: rgb(98, 114, 164);\n"
"  border-radius:15px;\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 15px;\n"
"  cursor: pointer;\n"
"  float: left;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"    background-color: rgb(18, 114, 164);\n"
"}")
        self.RADAR.setObjectName("RADAR")
        self.RADAR_2 = QtWidgets.QPushButton(self.dropShadowFrame)
        self.RADAR_2.setGeometry(QtCore.QRect(240, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.RADAR_2.setFont(font)
        self.RADAR_2.setStyleSheet(".QPushButton{\n"
"background-color: rgb(98, 114, 164);\n"
"  border-radius:15px;\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 15px;\n"
"  cursor: pointer;\n"
"  float: left;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"    background-color: rgb(18, 114, 164);\n"
"}")
        self.RADAR_2.setObjectName("RADAR_2")
        self.RADAR_3 = QtWidgets.QPushButton(self.dropShadowFrame)
        self.RADAR_3.setGeometry(QtCore.QRect(240, 240, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.RADAR_3.setFont(font)
        self.RADAR_3.setStyleSheet(".QPushButton{\n"
"background-color: rgb(98, 114, 164);\n"
"  border-radius:15px;\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 15px;\n"
"  cursor: pointer;\n"
"  float: left;\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"    background-color: rgb(18, 114, 164);\n"
"}")
        self.RADAR_3.setObjectName("RADAR_3")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">ONE BYTE CHEATS</span></p></body></html>"))
        self.label_description.setText(_translate("SplashScreen", "<html><head/><body><p>Cheats that use only one byte of cs go.</p></body></html>"))
        self.RADAR.setText(_translate("SplashScreen", "RADAR"))
        self.RADAR.clicked.connect(self.inject)
        self.RADAR_2.setText(_translate("SplashScreen", "WALLHACK"))
        self.RADAR_2.clicked.connect(self.inject2)
        self.RADAR_3.setText(_translate("SplashScreen", "MONEYCHECK"))
        self.RADAR_3.clicked.connect(self.inject3)


    def inject2(self):
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                                clientModule).start() + 2

        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()

    def inject3(self):
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                clientModule).start()

        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        pm.close_process()

    def inject(self):
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08',
                                                clientModule).start() + 6

        pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
        pm.close_process()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
