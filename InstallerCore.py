from welcom import Ui_welcome, QWidget
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMessageBox, QPushButton

def showMessageBox(parent, icon, title, text, buttons_text):
    msg_box = QMessageBox(parent)
    msg_box.setStyleSheet('''
QWidget {
    background-color: #ffffff;
    color: #202020;
    font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
    font-size: 14px;
}

QPushButton {
    background-color: #41b883;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 6px;
}
QPushButton:hover {
    background-color: #3cae78;
}
QPushButton:pressed {
    background-color: #359f6c;
}
QPushButton:disabled {
    background-color: #cccccc;
    color: #888888;
}

QLineEdit {
    background-color: white;
    border: 1px solid #c6c6c6;
    border-radius: 4px;
    padding: 4px 8px;
}
QLineEdit:focus {
    border: 1px solid #41b883;
}

QLabel {
    color: #202020;
}

QComboBox {
    background-color: white;
    border: 1px solid #c6c6c6;
    border-radius: 4px;
    padding: 4px 8px;
}
QComboBox:hover {
    border: 1px solid #41b883;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #c6c6c6;
}
QComboBox QAbstractItemView {
    background-color: white;
    border: 1px solid #c6c6c6;
    selection-background-color: #41b883;
    selection-color: white;
}

QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: #c6c6c6;
    border-radius: 5px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background: #a6a6a6;
}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}

QFrame#Card {
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 8px;
}

QCheckBox {
    spacing: 6px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
}
QCheckBox::indicator:unchecked {
    border: 1px solid #666;
    background-color: white;
    border-radius: 3px;
}
QCheckBox::indicator:checked {
    background-color: #41b883;
    border: 1px solid #41b883;
    image: url(:/icons/check_white.png); /* 可选 */
}
''')
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setIcon(icon)

    buttons_map = {}
    for button_text in buttons_text:
        button = QPushButton(button_text)
        
        lower_text = button_text.lower()
        if '确定' in lower_text or 'ok' in lower_text:
            role = QMessageBox.ButtonRole.AcceptRole
        elif '取消' in lower_text or 'cancel' in lower_text:
            role = QMessageBox.ButtonRole.RejectRole
        elif '关闭' in lower_text or 'close' in lower_text:
            role = QMessageBox.ButtonRole.RejectRole
        else:
            role = QMessageBox.ButtonRole.ActionRole

        msg_box.addButton(button, role)
        buttons_map[button] = button_text

    clicked_button = msg_box.exec()
    return buttons_map.get(msg_box.clickedButton(), None)

class WelcomPage(QWidget, Ui_welcome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class InstallerCore(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(531, 266)
        self.setWindowTitle("QYBot 安装程序")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.stack = QStackedWidget(self)
        self.welcome_page = WelcomPage()
        self.welcome_page.cancel_button.clicked.connect(self.close)
        self.stack.addWidget(self.welcome_page)

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.welcome_page)


    def closeEvent(self, event):
        reply = showMessageBox(self, QMessageBox.Warning, "退出", "安装尚未完成，你确定要退出安装程序吗？", ["确定", "取消"])
        if reply == "确定":
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    installer = InstallerCore()
    installer.show()
    sys.exit(app.exec())
