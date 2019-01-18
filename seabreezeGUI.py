# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GoogleDrive\ANMSA Projects\SeaBreezeApplication\seabreezeGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import seabreeze.spectrometers as sb

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(715, 380)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(170, 10, 501, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.record_spectrum)
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setValidator(QtGui.QDoubleValidator())
        self.textEdit.setText("1")
        # self.textEdit.textChanged.connect(self.set_integration_time)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.set_integration_time)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 10, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(self.get_spectrometer_list())
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.set_spectrometer)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SeaBreeze Application"))
        self.pushButton.setText(_translate("Dialog", "Record Spectrum"))
        self.pushButton_2.setText(_translate("Dialog", "Set Integration Time (s)"))
        self.pushButton_3.setText(_translate("Dialog", "Select Spectrometer"))
        self.pushButton_4.setText(_translate("Dialog", "Save Current Spectrum"))
    
    def set_integration_time(self):
        self.integration_time = float(self.textEdit.text())*1000
        self.alert_message("Integration time set to : " + str(self.integration_time) + " ms")

    def get_spectrometer_list(self):
        try:
            spectrometers = sb.list_devices()
            spectrometer_list=[]
            for spec in spectrometers:
                spectrometer_list.append(str(spec))
        except:
            spectrometer_list = "No devices found"
        return spectrometer_list

    def set_spectrometer(self):
        spectrometers = sb.list_devices()
        for spec in spectrometers:
            if str(spec) == self.comboBox.currentText(): 
                try:  
                    self.spectrometer = sb.Spectrometer(spec)
                    self.alert_message("Connected to: " + str(spec))
                except:
                    pass    

    def record_spectrum(self):
        # try:
        self.spectrometer.integration_time_micros(1000)
        #     self.alert_message(self.spectrometer.intensities())
        # except:
        #     self.alert_message("Unable to record Spectrum")

    def alert_message(self, message):
        self.alertMessage = QtWidgets.QMessageBox()
        self.alertMessage.setIcon(QtWidgets.QMessageBox.Warning)
        self.alertMessage.setText(message)
        self.alertMessage.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

