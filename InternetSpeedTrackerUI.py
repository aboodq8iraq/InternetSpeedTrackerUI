from PyQt5 import QtCore, QtGui, QtWidgets
from os import name

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 814)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 301, 821))
        self.frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 44, 111, 255), stop:1 rgba(28, 29, 73, 255));\n"
            "border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 760, 211, 41))
        self.label.setStyleSheet("background-color:none;\n"
                                 "color: rgb(165, 165, 165);\n"
                                 "font: 9pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 20, 16, 16))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(255, 0, 4);\n"
                                      "border:none;\n"
                                      "border-radius:8px;}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(125, 14, 20);\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 20, 16, 16))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(255, 255, 0);\n"
                                        "border:none;\n"
                                        "border-radius:8px;}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(207, 214, 71);\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 60, 161, 161))
        self.frame_2.setStyleSheet("QFrame{background-color:none;\n"
                                   "border:3px solid rgb(56, 59, 149);\n"
                                   "border-radius:80px;}\n"
                                   "QFrame:hover{\n"
                                   "border:2px solid rgb(56, 59, 149);\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(-30, 50, 221, 61))
        self.label_4.setStyleSheet("background-color:none;\n"
                                   "color: rgb(165, 165, 165);\n"
                                   "font: 35pt \"Segoe UI\";\n"
                                   "border:none;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 221, 41))
        self.label_2.setStyleSheet("background-color:none;\n"
                                   "color: rgb(165, 165, 165);\n"
                                   "font: 9pt \"Segoe UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 480, 221, 31))
        self.label_3.setStyleSheet("background-color:none;\n"
                                   "color: rgb(165, 165, 165);\n"
                                   "font: 9pt \"Segoe UI\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 700, 201, 41))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(72, 76, 191);\n" 
"color:white;\n" 
"border:none;\n" 
"border-radius:4px;\n" 
"font: 9pt \"Segoe UI\";}\n" 
"QPushButton:hover{\n" 
"border:1px solid rgb(37, 39, 99);\n" 
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(70, 300, 161, 161))
        self.frame_3.setStyleSheet("QFrame{background-color:none;\n" 
"border:3px solid rgb(56, 59, 149);\n" 
"border-radius:80px;}\n" 
"QFrame:hover{\n" 
"border:2px solid rgb(56, 59, 149);\n" 
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(-30, 50, 221, 61))
        self.label_5.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 35pt \"Segoe UI\";\n" 
"border:none;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 560, 101, 31))
        self.label_7.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 9pt \"Segoe UI\";")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(110, 560, 121, 31))
        self.label_8.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 8pt \"Segoe UI\";")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 590, 101, 41))
        self.label_9.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 9pt \"Segoe UI\";")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(90, 600, 181, 21))
        self.label_10.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 8pt \"Segoe UI\";")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(50, 620, 101, 51))
        self.label_11.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 9pt \"Segoe UI\";")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(120, 630, 161, 31))
        self.label_12.setStyleSheet("background-color:none;\n" 
"color: rgb(165, 165, 165);\n" 
"font: 8pt \"Segoe UI\";")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Internet Speed Tracker"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Upload"))
        self.pushButton_3.setText(_translate("MainWindow", "Get Speed"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Status  :"))
        self.label_8.setText(_translate("MainWindow", "None"))
        self.label_9.setText(_translate("MainWindow", "City :"))
        self.label_10.setText(_translate("MainWindow", "None"))
        self.label_11.setText(_translate("MainWindow", "Sponsor : "))
        self.label_12.setText(_translate("MainWindow", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())