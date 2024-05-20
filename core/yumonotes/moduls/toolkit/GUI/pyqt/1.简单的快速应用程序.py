import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


# 声明式UI
# 使用QML语言
QML = """   
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 300
    height: 200
    visible: true
    title: "Hello World"

    readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
                                           "Hola Mundo", "Привет мир"]

    function setText() {
        var i = Math.round(Math.random() * 3)
        text.text = texts[i]
    }

    ColumnLayout {
        anchors.fill:  parent

        Text {
            id: text
            text: "Hello World"
            Layout.alignment: Qt.AlignHCenter
        }
        Button {
            text: "Click me"
            Layout.alignment: Qt.AlignHCenter
            onClicked:  setText()
        }
    }
}
"""


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)         # 创建QtGui应用程序对象
    engine = QQmlApplicationEngine()        # 创建引擎
    engine.loadData(QML.encode('utf-8'))    # 导入QML文件， 基于文件创建GUI

    if not engine.rootObjects():
        sys.exit()

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)