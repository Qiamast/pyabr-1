import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: dmgr
    visible: true
    color: "white"
    width: 600
    height: 500
    title: "Downloads"

    ToolBar {
        id: toolbar
        anchors.top: parent.top
        width: parent.width
        height: 70

        RowLayout {
                    anchors.verticalCenter: parent.verticalCenter

            ToolButton {
                icon.source: 'file:///stor/usr/share/icons/breeze-new.svg'
                icon.color: "white"
                id: add
                objectName: "add"
            }

        }
    }

    ScrollView {
        width: parent.width
        height: parent.height-80
        anchors.topMargin: 10
        anchors.top: toolbar.bottom
        clip: true
        id: scroll
        Column {
            width: dmgr.width
            height: dmgr.height-70
            spacing: 2
            Repeater {
                model: FileModel

                Rectangle {

                    width: parent.width
                    height: parent.width/10
                    color: "transparent"

                    Image {
                            source: model.logo
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                    }

                    Text {
                        text: model.name
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Text {
                        text: model.mimetype
                        font.family: "IRANSans"
                        font.pixelSize: 14
                        color: "gray"
                        anchors.right: parent.right
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.rightMargin: 100
                    }
                   
                    Text {
                        text: model.size
                        font.family: "IRANSans"
                        font.pixelSize: 14
                        color: "gray"
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.leftMargin: 20
                        anchors.rightMargin: 20
                    }

                    Rectangle {
                        width: parent.width
                        height: 1
                        color: "silver"
                        anchors.top: parent.bottom
                    }
                }
            }
        }
    }
}