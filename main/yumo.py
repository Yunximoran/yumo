import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QCheckBox,
    QLineEdit,
    QInputDialog,
    QMenu,
    QMenuBar,
)
from PyQt6.QtGui import QIcon, QAction

from lib.datastructure.list.unordered import UnorderedList
from lib.datastructure.basic.stack import Stack

APPLICATION = QApplication(sys.argv)

X = 10
Y = 30
WIDTH = 1226
HEIGHT = 648


class YuMoDesktop(QWidget):

    # 绑定的事件，会在代码执行完后触发窗口中的事件才会触发，所有有些事后可以忽略创建顺序

    def __init__(self):
        super().__init__()

        self.init()

        sys.exit(APPLICATION.exec())

    def init(self):
        """
        QWidgets，默认创建分区，比如状态栏，菜单栏这类的区域
        导入对应的包，获取需要的分区对象，对其进行修改
        :return:
        """
        self.load_widgets()
        self.load_config()
        self.setGeometry(X, Y, WIDTH, HEIGHT)
        self.setWindowTitle("YuMo First GUI")
        self.setWindowOpacity(0.7)
        self.show()

    def load_widgets(self):
        Menu(self)

    def load_config(self):
        self.setStyleSheet("background-color: #822128; color: #fff")
        # 红 绿 蓝

    # def __menu(self):
    #     menu = QMenuBar(self)  # 激活菜单栏
    #     Menu(menu)
    #
    # self.firstMenu1 = QMenu("File", self)
    # self.firstMenu2 = QMenu("Project", self)
    #
    # self.__firstMenuAct_1()
    # self.__firstMenuAct_2()
    #
    # menu.addMenu(self.firstMenu1)
    # menu.addMenu(self.firstMenu2)

    # def __firstMenuAct_1(self):
    #     act_1 = QAction("Open", self.firstMenu1)
    #     act_2 = QAction("Save", self.firstMenu1)
    #     self.firstMenu1.addActions([act_1, act_2])
    #
    # def __firstMenuAct_2(self):
    #     act_1 = QAction("Create", self.firstMenu2)
    #     act_2 = QAction("Load", self.firstMenu2)
    #
    #     self.firstMenu2.addActions([act_1, act_2])


class Menu:
    # 递归创建菜单栏， 传入参数{一个分层字典}

    MENU_LEVEL = {
        "file": {
            "file attribute": {
                "encode": "UTF-8",
                "add BOM": None
            },
            "restruct": None
        },
        "edit": {
            "copy": "Ctrl+C"
        }
    }

    MENU_STACK = Stack()

    def __init__(self, BASE: QWidget):
        self.widget = BASE
        self.MENU = QMenuBar(BASE)
        # self.first()
        self.init()
        print(self.MENU_LEVEL)

    def init(self, MenuStruct=MENU_LEVEL, level=0):
        if len(self.MENU_STACK) == 0:
            print("root MenuStruct")
            parent = self.MENU
        else:
            parent, Name = self.MENU_STACK.pop()
            print(Name)

        childActs = []
        for NextNode in MenuStruct:
            print(f"Current: {NextNode}, level:{level}")
            if isinstance(MenuStruct[NextNode], dict):
                childMenu = QMenu(NextNode, parent)  # 创建子菜单
                parent.addMenu(childMenu)
                self.MENU_STACK.push((childMenu, NextNode))  # 将子菜单添加进Stack
                self.init(MenuStruct[NextNode], level + 1)  # 递归init方法
            else:
                childAct = QAction(NextNode, parent)
                MenuStruct[NextNode] = childAct  # 记录childAct，方便后面对其进行绑定
                # parent.addAction(childAct)
                childActs.append(childAct)

        parent.addActions(childActs)

    # 后面对QAction的维护？
    def bandEvent(self, Act, Event):
        """
            应该有个东西保存所有的QAction
        :param Act:
        :param Event:
        :return:
        """
        pass

    def first(self):
        firstMenu = QMenu("Menu", self.MENU)  # 这里的绑定到MENU 和 WIDGET 都没有关系，推测绑定可能存在连接关系
        self.join(firstMenu, self.MENU)

    @staticmethod
    def join(child, parent):
        """
        :param parent:
        :param child:
        :type parent: QMenuBar
        :type child: QMenu
        :return:
        """
        parent.addMenu(child)  # 这可以传入多个child addMenu的型参 *__args


class Button:
    # 按钮
    def __init__(self):
        pass


if __name__ == '__main__':
    YuMoDesktop()
