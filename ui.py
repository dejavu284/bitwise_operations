# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_lab8.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_zero = QtWidgets.QWidget()
        self.tab_zero.setObjectName("tab_zero")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_zero)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(self.tab_zero)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.tab_zero)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.first_value_line = QtWidgets.QLineEdit(self.tab_zero)
        self.first_value_line.setAlignment(QtCore.Qt.AlignCenter)
        self.first_value_line.setObjectName("first_value_line")
        self.horizontalLayout_2.addWidget(self.first_value_line)
        self.second_value_line = QtWidgets.QLineEdit(self.tab_zero)
        self.second_value_line.setAlignment(QtCore.Qt.AlignCenter)
        self.second_value_line.setObjectName("second_value_line")
        self.horizontalLayout_2.addWidget(self.second_value_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.some_output_1 = QtWidgets.QLabel(self.tab_zero)
        self.some_output_1.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_1.setObjectName("some_output_1")
        self.verticalLayout_3.addWidget(self.some_output_1)
        self.some_output_2 = QtWidgets.QLabel(self.tab_zero)
        self.some_output_2.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_2.setObjectName("some_output_2")
        self.verticalLayout_3.addWidget(self.some_output_2)
        self.some_output_3 = QtWidgets.QLabel(self.tab_zero)
        self.some_output_3.setEnabled(True)
        self.some_output_3.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_3.setObjectName("some_output_3")
        self.verticalLayout_3.addWidget(self.some_output_3)
        self.some_output_4 = QtWidgets.QLabel(self.tab_zero)
        self.some_output_4.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_4.setObjectName("some_output_4")
        self.verticalLayout_3.addWidget(self.some_output_4)
        self.custom_btn = QtWidgets.QPushButton(self.tab_zero)
        self.custom_btn.setObjectName("custom_btn")
        self.verticalLayout_3.addWidget(self.custom_btn)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_zero, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 3, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 1, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_1)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.some_output_5 = QtWidgets.QLabel(self.tab_1)
        self.some_output_5.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_5.setObjectName("some_output_5")
        self.verticalLayout_4.addWidget(self.some_output_5)
        self.some_output_6 = QtWidgets.QLabel(self.tab_1)
        self.some_output_6.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_6.setObjectName("some_output_6")
        self.verticalLayout_4.addWidget(self.some_output_6)
        self.some_output_7 = QtWidgets.QLabel(self.tab_1)
        self.some_output_7.setEnabled(True)
        self.some_output_7.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_7.setObjectName("some_output_7")
        self.verticalLayout_4.addWidget(self.some_output_7)
        self.some_output_8 = QtWidgets.QLabel(self.tab_1)
        self.some_output_8.setAlignment(QtCore.Qt.AlignCenter)
        self.some_output_8.setObjectName("some_output_8")
        self.verticalLayout_4.addWidget(self.some_output_8)
        self.test_btn = QtWidgets.QPushButton(self.tab_1)
        self.test_btn.setObjectName("test_btn")
        self.verticalLayout_4.addWidget(self.test_btn)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_1, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Input first value"))
        self.label_2.setText(_translate("MainWindow", "Input second value"))
        self.some_output_1.setText(_translate("MainWindow", "decimal_values"))
        self.some_output_2.setText(_translate("MainWindow", "Solution"))
        self.some_output_3.setText(_translate("MainWindow", "Count_iter"))
        self.some_output_4.setText(_translate("MainWindow", "Result"))
        self.custom_btn.setText(_translate("MainWindow", "Find "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zero), _translate("MainWindow", "Custom"))
        self.radioButton_6.setText(_translate("MainWindow", "Sixth_test"))
        self.radioButton_3.setText(_translate("MainWindow", "Third_test"))
        self.radioButton_1.setText(_translate("MainWindow", "First_test"))
        self.radioButton_4.setText(_translate("MainWindow", "Fourth_test"))
        self.radioButton_2.setText(_translate("MainWindow", "Second_test"))
        self.radioButton_5.setText(_translate("MainWindow", "Fifth_test"))
        self.some_output_5.setText(_translate("MainWindow", "decimal_values "))
        self.some_output_6.setText(_translate("MainWindow", "Solution"))
        self.some_output_7.setText(_translate("MainWindow", "Count_iter"))
        self.some_output_8.setText(_translate("MainWindow", "Result"))
        self.test_btn.setText(_translate("MainWindow", "Find "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "test\'s"))
