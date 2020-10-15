# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shake_test_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import resource_rc

class Ui_ShakeTestWindow(object):
    def setupUi(self, ShakeTestWindow):
        if not ShakeTestWindow.objectName():
            ShakeTestWindow.setObjectName(u"ShakeTestWindow")
        ShakeTestWindow.resize(1034, 653)
        self.actionstart = QAction(ShakeTestWindow)
        self.actionstart.setObjectName(u"actionstart")
        icon = QIcon()
        icon.addFile(u":/tool_icon/resource/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionstart.setIcon(icon)
        self.actionpause = QAction(ShakeTestWindow)
        self.actionpause.setObjectName(u"actionpause")
        icon1 = QIcon()
        icon1.addFile(u":/tool_icon/resource/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionpause.setIcon(icon1)
        self.actionrestart = QAction(ShakeTestWindow)
        self.actionrestart.setObjectName(u"actionrestart")
        icon2 = QIcon()
        icon2.addFile(u":/tool_icon/resource/restart .png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionrestart.setIcon(icon2)
        self.actionspeedup = QAction(ShakeTestWindow)
        self.actionspeedup.setObjectName(u"actionspeedup")
        icon3 = QIcon()
        icon3.addFile(u":/tool_icon/resource/\u5feb\u8fdb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionspeedup.setIcon(icon3)
        self.actionspeeddown = QAction(ShakeTestWindow)
        self.actionspeeddown.setObjectName(u"actionspeeddown")
        icon4 = QIcon()
        icon4.addFile(u":/tool_icon/resource/\u5feb\u9000.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionspeeddown.setIcon(icon4)
        self.actionadd = QAction(ShakeTestWindow)
        self.actionadd.setObjectName(u"actionadd")
        icon5 = QIcon()
        icon5.addFile(u":/tool_icon/resource/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd.setIcon(icon5)
        self.actionsubtract = QAction(ShakeTestWindow)
        self.actionsubtract.setObjectName(u"actionsubtract")
        icon6 = QIcon()
        icon6.addFile(u":/tool_icon/resource/subtract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsubtract.setIcon(icon6)
        self.centralwidget = QWidget(ShakeTestWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        ShakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShakeTestWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1034, 22))
        ShakeTestWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShakeTestWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShakeTestWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(ShakeTestWindow)
        self.toolBar.setObjectName(u"toolBar")
        ShakeTestWindow.addToolBar(Qt.RightToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionstart)
        self.toolBar.addAction(self.actionpause)
        self.toolBar.addAction(self.actionrestart)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionadd)
        self.toolBar.addAction(self.actionsubtract)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionspeedup)
        self.toolBar.addAction(self.actionspeeddown)

        self.retranslateUi(ShakeTestWindow)

        QMetaObject.connectSlotsByName(ShakeTestWindow)
    # setupUi

    def retranslateUi(self, ShakeTestWindow):
        ShakeTestWindow.setWindowTitle(QCoreApplication.translate("ShakeTestWindow", u"\u89c6\u9891\u5bf9\u6bd4\u5de5\u5177", None))
        self.actionstart.setText(QCoreApplication.translate("ShakeTestWindow", u"start", None))
#if QT_CONFIG(tooltip)
        self.actionstart.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u5f00\u59cb", None))
#endif // QT_CONFIG(tooltip)
        self.actionpause.setText(QCoreApplication.translate("ShakeTestWindow", u"pause", None))
#if QT_CONFIG(tooltip)
        self.actionpause.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u6682\u505c", None))
#endif // QT_CONFIG(tooltip)
        self.actionrestart.setText(QCoreApplication.translate("ShakeTestWindow", u"restart", None))
#if QT_CONFIG(tooltip)
        self.actionrestart.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u91cd\u65b0\u5f00\u59cb", None))
#endif // QT_CONFIG(tooltip)
        self.actionspeedup.setText(QCoreApplication.translate("ShakeTestWindow", u"speedup", None))
#if QT_CONFIG(tooltip)
        self.actionspeedup.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u52a0\u901f", None))
#endif // QT_CONFIG(tooltip)
        self.actionspeeddown.setText(QCoreApplication.translate("ShakeTestWindow", u"speeddown", None))
#if QT_CONFIG(tooltip)
        self.actionspeeddown.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u51cf\u901f", None))
#endif // QT_CONFIG(tooltip)
        self.actionadd.setText(QCoreApplication.translate("ShakeTestWindow", u"add", None))
#if QT_CONFIG(tooltip)
        self.actionadd.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u589e\u52a0\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.actionsubtract.setText(QCoreApplication.translate("ShakeTestWindow", u"subtract", None))
#if QT_CONFIG(tooltip)
        self.actionsubtract.setToolTip(QCoreApplication.translate("ShakeTestWindow", u"\u51cf\u5c11\u89c6\u9891", None))
#endif // QT_CONFIG(tooltip)
        self.toolBar.setWindowTitle(QCoreApplication.translate("ShakeTestWindow", u"toolBar", None))
    # retranslateUi

