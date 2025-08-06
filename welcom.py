# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcom.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_welcome(object):
    def setupUi(self, welcome):
        if not welcome.objectName():
            welcome.setObjectName(u"welcome")
        welcome.resize(531, 266)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        welcome.setFont(font)
        welcome.setStyleSheet(u"/* \u57fa\u7840\u901a\u7528 */\n"
"QWidget {\n"
"    background-color: #ffffff;\n"
"    color: #202020;\n"
"    font-family: \"Segoe UI\", \"Microsoft YaHei\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #41b883;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3cae78;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #359f6c;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #cccccc;\n"
"    color: #888888;\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #c6c6c6;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #41b883;\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #202020;\n"
"}\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #c6c6c6;\n"
"   "
                        " border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 1px solid #41b883;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #c6c6c6;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    border: 1px solid #c6c6c6;\n"
"    selection-background-color: #41b883;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* QScrollBar\uff08\u7eb5\u5411\uff09 */\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #c6c6c6;\n"
"    border-radius: 5px;\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a6a6a6;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
""
                        "}\n"
"\n"
"/* QFrame#Card \uff08\u81ea\u5b9a\u4e49\u5361\u7247\uff09 */\n"
"QFrame#Card {\n"
"    background-color: white;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox {\n"
"    spacing: 6px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #666;\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #41b883;\n"
"    border: 1px solid #41b883;\n"
"    image: url(:/icons/check_white.png); /* \u53ef\u9009 */\n"
"}\n"
"")
        self.label = QLabel(welcome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 24, 291, 141))
        self.horizontalLayoutWidget = QWidget(welcome)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(300, 210, 211, 33))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel_button = QPushButton(self.horizontalLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.next_button = QPushButton(self.horizontalLayoutWidget)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout.addWidget(self.next_button)

        self.label_2 = QLabel(welcome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 20, 221, 221))
        self.label_2.setPixmap(QPixmap(u"Icon.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(welcome)

        QMetaObject.connectSlotsByName(welcome)
    # setupUi

    def retranslateUi(self, welcome):
        welcome.setWindowTitle(QCoreApplication.translate("welcome", u"Form", None))
        self.label.setText(QCoreApplication.translate("welcome", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700; color:#34495e;\">\u6b22\u8fce\uff01</span></p><p><span style=\" font-size:12pt; color:#34495e;\">\u6b64\u5b89\u88c5\u5411\u5bfc\u5c06\u5f15\u5bfc\u4f60\u5b89\u88c5 QYBot\u3002</span></p><p><span style=\" font-size:12pt; color:#34495e;\">\u8981\u7ee7\u7eed\uff0c\u8bf7\u70b9\u51fb\u4e0b\u4e00\u6b65\u3002</span></p></body></html>", None))
        self.cancel_button.setText(QCoreApplication.translate("welcome", u"\u53d6\u6d88", None))
        self.next_button.setText(QCoreApplication.translate("welcome", u"\u4e0b\u4e00\u6b65", None))
        self.label_2.setText("")
    # retranslateUi

