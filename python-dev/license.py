# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'license.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_license(object):
    def setupUi(self, license):
        if not license.objectName():
            license.setObjectName(u"license")
        license.resize(531, 266)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        license.setFont(font)
        license.setStyleSheet(u"/* \u57fa\u7840\u901a\u7528 */\n"
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
"    border-radius: 3px;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(license)
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
        self.next_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.next_button)

        self.label_2 = QLabel(license)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 20, 221, 221))
        self.label_2.setPixmap(QPixmap(u"Icon.png"))
        self.label_2.setScaledContents(True)
        self.textEdit = QTextEdit(license)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 20, 291, 141))
        self.textEdit.setReadOnly(True)
        self.checkBox = QCheckBox(license)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(220, 170, 221, 20))

        self.retranslateUi(license)

        QMetaObject.connectSlotsByName(license)
    # setupUi

    def retranslateUi(self, license):
        license.setWindowTitle(QCoreApplication.translate("license", u"Form", None))
        self.cancel_button.setText(QCoreApplication.translate("license", u"\u53d6\u6d88", None))
        self.next_button.setText(QCoreApplication.translate("license", u"\u4e0b\u4e00\u6b65", None))
        self.label_2.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("license", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Microsoft YaHei','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">QYbot \u4f7f\u7528\u8bb8\u53ef\u534f\u8bae</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-size:14px;\">\u7b2c\u4e00\u7ae0 \u6570\u636e\u5b89\u5168\u58f0\u660e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">1.1 \u9879\u76ee\u6027\u8d28</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">QYbot \u662f\u4e00\u4e2a\u5f00\u6e90\u7684\u673a\u5668\u4eba\u6846\u67b6\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u9879\u76ee\u6e90\u7801\u6258\u7ba1\u4e8e GitHub\uff1a[https://github.com/iYeXin/qybot/](https://github.com/iYeXin/qybot/)</span></p>\n"
"<"
                        "p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u9075\u5faa MIT \u5f00\u6e90\u8bb8\u53ef\u8bc1\uff08[\u67e5\u770b\u8bb8\u53ef\u8bc1](https://github.com/iYeXin/qybot/blob/main/LICENSE)\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u63a5\u53d7\u793e\u533a\u4ee3\u7801\u5ba1\u8ba1\u4e0e\u529f\u80fd\u8d21\u732e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">1.2 \u51ed\u8bc1\u9690\u79c1\u4fdd\u62a4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u7528\u6237\u8f93\u5165\u7684 QQ \u5f00\u653e\u5e73\u53f0 `AppID` \u548c `AppSecret` \u4ec5\u7528\u4e8e\u673a\u5668\u4eba\u8eab\u4efd\u9a8c\u8bc1\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u51ed\u8bc1\u5b8c\u5168\u5b58\u50a8\u4e8e\u7528\u6237\u672c\u5730\u8bbe\u5907</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u6846\u67b6\u6c38\u4e0d\u6536\u96c6\u3001\u4e0d\u4e0a\u4f20\u4efb\u4f55\u7528\u6237\u51ed\u8bc1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u51ed\u8bc1\u4ec5\u7528\u4e8e\u4e0e QQ \u5e73\u53f0\u8fdb\u884c\u901a\u4fe1</span></p>\n"
"<p style=\"-qt-paragraph-typ"
                        "e:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">1.3 \u8fd0\u884c\u73af\u5883\u9694\u79bb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u5b89\u88c5\u5305\u6267\u884c\u8fc7\u7a0b\u6ee1\u8db3\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u6240\u6709\u4f9d\u8d56\uff08Chrome/Node.js\uff09\u5747\u4ece\u5b98\u65b9\u6e90\u4e0b\u8f7d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u4e0d\u690d\u5165\u4efb\u4f55\u540e"
                        "\u95e8\u6216\u6570\u636e\u91c7\u96c6\u6a21\u5757</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u7f51\u7edc\u901a\u4fe1\u4ec5\u8fde\u63a5 QQ \u5b98\u65b9 API \u548c\u7528\u6237\u6307\u5b9a\u7684\u63d2\u4ef6\u670d\u52a1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u7b2c\u4e8c\u7ae0 \u63d2\u4ef6\u5b89\u5168\u58f0\u660e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:14px;\">2.1 \u63d2\u4ef6\u5e02\u573a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">[\u63d2\u4ef6\u5e02\u573a](https://market.qybot.yexin.wiki/)\u5e73\u53f0\u4ec5\u63d0\u4f9b\u5206\u53d1\u670d\u52a1\uff0c\u65e0\u6cd5\u4fdd\u8bc1\u5b89\u5168\u6027</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">2.2 \u7528\u6237\u8d23\u4efb</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u4f7f\u7528\u63d2\u4ef6\u65f6\u8bf7\u6ce8\u610f\uff1a</span></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">! \u8b66\u544a  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">1. \u63d2\u4ef6\u53ef\u80fd\u8981\u6c42\u63d0\u4f9b API_KEY/\u8d26\u53f7\u5bc6\u7801\u7b49\u654f\u611f\u4fe1\u606f  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">2. \u6211\u4eec**\u65e0\u6cd5\u5b8c\u5168\u9a8c\u8bc1**\u7b2c\u4e09\u65b9\u63d2\u4ef6\u7684\u5b89\u5168\u6027  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">3. \u8bf7\u81ea\u884c\u8bc4\u4f30\u63d2\u4ef6\u6765\u6e90\u53ef\u4fe1\u5ea6  </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">2.3 \u5173\u952e\u5efa\u8bae</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u5728\u6c99\u76d2\u73af\u5883\u6d4b\u8bd5\u65b0\u63d2\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u5b9a\u671f\u5ba1\u67e5\u63d2\u4ef6\u914d\u7f6e\uff08`/plugins/*/config.*`\uff09</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u7b2c\u4e09\u7ae0 \u514d\u8d23\u6761\u6b3e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">3.1 \u8d23\u4efb\u8303\u56f4\u754c\u5b9a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u4e0b\u5217\u60c5\u51b5\u9020\u6210\u7684\u635f\u5931\u6982\u4e0d\u627f\u62c5\u8d23\u4efb\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">1. \u56e0\u63d2\u4ef6\u6f0f\u6d1e\u5bfc\u81f4\u7684\u6570\u636e\u6cc4\u9732  </span></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">2. \u672a\u53ca\u65f6\u66f4\u65b0IP\u767d\u540d\u5355\u9020\u6210\u7684\u670d\u52a1\u4e2d\u65ad  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">3. \u4f7f\u7528\u975e\u5b98\u65b9\u6e20\u9053\u83b7\u53d6\u7684\u63d2\u4ef6  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">4. \u672a\u9075\u5b88QQ\u5f00\u653e\u5e73\u53f0\u89c4\u5219\u5bfc\u81f4\u7684\u5c01\u53f7  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">5. \u5bb6\u7528\u5bbd\u5e26IP\u53d8\u66f4\u672a\u53ca\u65f6\u5904\u7406\u7684\u6545\u969c  </span></p"
                        ">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">3.2 \u635f\u5931\u8d54\u507f\u6392\u9664</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u6211\u4eec\u4e0d\u627f\u62c5\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u95f4\u63a5\u635f\u5931\uff08\u5229\u6da6\u635f\u5931/\u4e1a\u52a1\u4e2d\u65ad\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u63d2\u4ef6\u6ee5\u7528\u5bfc"
                        "\u81f4\u7684\u5904\u7f5a\u91d1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u7528\u6237\u51ed\u8bc1\u6cc4\u9732\u5f15\u53d1\u7684\u8fde\u5e26\u8d23\u4efb</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u7b2c\u56db\u7ae0 \u534f\u8bae\u751f\u6548</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">4.1 \u751f\u6548\u65b9\u5f0f</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- \u60a8\u5728\u901a\u8fc7\u5b98\u7f51\u8fdb\u884c\u8d44\u6e90\u4e0b\u8f7d\u548c\u7a0b\u5e8f\u90e8\u7f72\u65f6\u9700\u9605\u8bfb\u672c\u534f\u8bae</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">- Windows \u5b89\u88c5\u5305\uff1a\u52fe\u9009 &quot;\u6211\u540c\u610f\u300aQYbot\u8bb8\u53ef\u534f\u8bae\u300b&quot; \u540e\u65b9\u53ef\u7ee7\u7eed\u5b89\u88c5</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("license", u"\u6211\u5df2\u7ecf\u9605\u8bfb\u5e76\u540c\u610f\u4ee5\u4e0a\u8bb8\u53ef\u534f\u8bae", None))
    # retranslateUi

