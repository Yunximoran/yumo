import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMenu,
    QPushButton,
    QLineEdit,
    QInputDialog,
    QMainWindow,
)
from PyQt6.QtGui import QAction, QIcon


class YuMo(QWidget):
    # 继承QWidget， self.就是一个Widget对象
    APPLICATION = QApplication(sys.argv)

    def __init__(self):
        super().__init__()
        self.Widget()

        self.setGeometry(30, 50, 450, 380)  # 位置，长宽
        self.setWindowTitle("YuMO Dialog")

        self.show()

        sys.exit(self.APPLICATION.exec())

    def Widget(self):
        # self.statusBar().showMessage("Ready") # statusBar不属于QWidget

        # 创建按钮并绑定事件
        self.btn = QPushButton("Click", self)  # 创建按钮组件
        self.btn.resize(98, 50)
        self.btn.move(20, 20)
        # self.btn.clicked.connect(self.Edit())  # 传递一个函数， 定义点击后发生的事件
        self.btn.clicked.connect(self.Edit)  # * 注意这里传入的函数不能带括号， 绑定按钮单击事件

        self.le = QLineEdit(self)
        self.le.move(130, 22)

    def Edit(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', "Enter your name:")  # 获取输入
        """
            # 该方法会弹出一个后去文本数据的文本框
        self.绑定的父上级组件
        ‘新窗口名称’，
        ‘QLabel’
        """

        if ok:  # 将输入返回的文本替换进TEXT框中
            # old = self.le.connectNotify()
            # print(old)
            self.le.setText(str(text))


class YuMoMainWindows(QMainWindow):
    APPLICATION = QApplication(sys.argv)

    def __init__(self):
        # QMenu 目录，集合
        # QAction 可触发选项
        super().__init__()

        exitAct = QAction(QIcon('exit.png'), "Exit", self)

        exitAct.setShortcut("Ctrl+Q")   # 设置快捷键
        exitAct.setStatusTip('Exit application')    # 设置状态提示
        exitAct.triggered.connect(QApplication.instance().quit)  # 组件对象，组件行为，组件绑定函数
        # triggered 触发， 启动

        self.statusBar().showMessage("This is YuMo Desktop Application")  # 创建状态栏
        # showMessage() 状态栏显示信息

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('File')  # 添加子菜单1
        fileMenu2 = menubar.addMenu("Test")  # 添加子菜单2

        impMenu = QMenu("Import", self)  # 创建菜单对象
        impAct = QAction("Import mail", self)  # 创建菜单事件
        impMenu.addAction(impAct)  # 将菜单事件绑定到菜单中

        newAct = QAction("new", self)

        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(30, 30, 600, 450)
        self.setWindowTitle('YuMo QMainWindows')
        self.show()

        sys.exit(self.APPLICATION.exec())


if __name__ == '__main__':
    YuMoMainWindows()