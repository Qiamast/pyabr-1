import QtQuick 2.0
import QtQuick.Window 2.3
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4
import QtQuick.Controls 1.2
import QtQuick.Controls 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.12

ApplicationWindow {
    id: file
    visible: true
    color: "white"
    width: 900
    height: 700

    Text {
        visible: false
        text: ''
        id: tsel
        objectName: "tsel"
    }
    
    ScrollView {
        width: parent.width
        height: parent.height-file.height/10
        anchors.topMargin: 10
        anchors.top: parent.top
        clip: true
        objectName: "ListView"
        id: scroll
        Column {
            width: file.width
            height: file.height-70-file.height/10
            spacing: 2
            Repeater {
                model: ShellThemeModel

                ToolButton {

                    width: parent.width
                    height: parent.width/10
                    //color: "transparent"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            file_anim.start();
                            tsel.text = model.name
                        }
                    }

                    Image {
                            source: model.logo
                            anchors.left: parent.left
                            anchors.leftMargin: 20
                            anchors.rightMargin: 20
                            width: parent.height
                            sourceSize: Qt.size( parent.width, parent.height )
                            height: parent.height
                            id: imagex
                            NumberAnimation on opacity {
                                id: file_anim
                                from: 0
                                to: 1
                                duration: 100
                            }
                    }

                    Text {
                        text: model.namex
                        font.family: "IRANSans"
                        font.pixelSize: 18
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: imagex.right
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
            anchors.bottom: cancel.top
        }
    }
    Button {
        id: cancel
        text: "Cancel"
        objectName: "btnCancel"
        width: parent.width/2
        height: parent.height/10
        anchors.bottomMargin: 0
        anchors.bottom: parent.bottom
        font.family: "IRANSans"
    }
    Button {
        text: "Change"
        objectName: "btnChange"
        width: parent.width/2
        enabled: false
        height: parent.height/10
        anchors.bottomMargin: 0
        font.family: "IRANSans"
        anchors.left: cancel.right
        anchors.bottom: parent.bottom
    }
}