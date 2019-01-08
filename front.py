# Frontend for LSB Steganography

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_mainWindow(object):

    # Init UI	
    def setupUi(self, mainWindow):
        
        # MainWindow
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

	  # Tab widget	
        self.etabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.etabWidget.setGeometry(QtCore.QRect(20, 10, 681, 521))
        self.etabWidget.setObjectName("etabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.elabel = QtWidgets.QLabel(self.tab)
        self.elabel.setGeometry(QtCore.QRect(40, 30, 342, 192))
        self.elabel.setObjectName("elabel")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(90, 360, 391, 111))
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(500, 290, 161, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Encode button		 
        self.encode = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.encode.setObjectName("encode")
        self.gridLayout.addWidget(self.encode, 2, 0, 1, 1)
        self.ebrowse = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ebrowse.setObjectName("ebrowse")
        self.gridLayout.addWidget(self.ebrowse, 1, 0, 1, 1)
        self.elineEdit = QtWidgets.QLineEdit(self.tab)
        self.elineEdit.setGeometry(QtCore.QRect(120, 300, 361, 20))
        self.elineEdit.setObjectName("elineEdit")
        self.epass = QtWidgets.QLineEdit(self.tab)
        self.epass.setGeometry(QtCore.QRect(120, 330, 361, 21))
        self.epass.setObjectName("epass")

        # Text Edit for image path
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 300, 51, 16))
        self.label.setObjectName("label")

        # Text Edit for Key
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 330, 61, 16))
        self.label_2.setObjectName("label_2")
        self.eerror = QtWidgets.QLabel(self.tab)
        self.eerror.setGeometry(QtCore.QRect(500, 410, 161, 71))
        self.eerror.setText("")
        self.eerror.setObjectName("eerror")
        self.etabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.dlabel = QtWidgets.QLabel(self.tab_2)
        self.dlabel.setGeometry(QtCore.QRect(40, 30, 342, 192))
        self.dlabel.setObjectName("dlabel")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(500, 290, 161, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
      
        # Decode button
        self.Decode = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Decode.setObjectName("Decode")
        self.gridLayout_2.addWidget(self.Decode, 2, 0, 1, 1)
        self.dbrowse = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dbrowse.setObjectName("dbrowse")
        self.gridLayout_2.addWidget(self.dbrowse, 0, 0, 1, 1)
        self.dlineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.dlineEdit.setGeometry(QtCore.QRect(120, 300, 361, 20))
        self.dlineEdit.setObjectName("dlineEdit")
        self.dtextEdit = QtWidgets.QTextEdit(self.tab_2)
        self.dtextEdit.setGeometry(QtCore.QRect(90, 360, 391, 111))
        self.dtextEdit.setObjectName("dtextEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(50, 330, 61, 16))
        self.label_4.setObjectName("label_4")
        self.dpass = QtWidgets.QLineEdit(self.tab_2)
        self.dpass.setGeometry(QtCore.QRect(120, 330, 361, 20))
        self.dpass.setObjectName("dpass")
        self.derror = QtWidgets.QLabel(self.tab_2)
        self.derror.setGeometry(QtCore.QRect(500, 410, 161, 61))
        self.derror.setText("")
        self.derror.setObjectName("derror")
        self.etabWidget.addTab(self.tab_2, "")
        mainWindow.setCentralWidget(self.centralwidget)

        # Menubar
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.etabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.elabel.setText(_translate("mainWindow", "                                               Image here"))
        self.textEdit.setPlaceholderText(_translate("mainWindow", "enter message here"))
        self.encode.setText(_translate("mainWindow", "Encode"))
        self.ebrowse.setText(_translate("mainWindow", "Browse"))

        # Text Edit for image path
        self.label.setText(_translate("mainWindow", "Location :"))

        # Text Edit for Key  
        self.label_2.setText(_translate("mainWindow", "Key : "))
        self.etabWidget.setTabText(self.etabWidget.indexOf(self.tab), _translate("mainWindow", "Encode"))
        self.dlabel.setText(_translate("mainWindow", "                                               Image here"))
        self.Decode.setText(_translate("mainWindow", "Decode"))
        self.dbrowse.setText(_translate("mainWindow", "Browse"))
        
# Text Edit for message		
self.dtextEdit.setPlaceholderText(_translate("mainWindow", "enter message here"))
        self.label_3.setText(_translate("mainWindow", "Location :"))
        self.label_4.setText(_translate("mainWindow", "Key : "))
        self.etabWidget.setTabText(self.etabWidget.indexOf(self.tab_2), _translate("mainWindow", "Decode"))