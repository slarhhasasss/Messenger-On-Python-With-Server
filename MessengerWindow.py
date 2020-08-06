# чтобы пользоваться этим файлом, необходимо заранее скомпилировать из файла messenger.ui файл clientui.py, так как
# наш файл наследуется от него. это нужно делать каждый раз, когда изменяем дизайн в QtDesigner. Для этого в терминале
# прописываем pyuic5 messenger.ui -o clientui.py
from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui

# Наследуем классы QtWidgets.QMainWindow and clientui.Ui_MainWindow
import utilies


class WindowMessenger(clientui.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # изначально кнопки недоступны, пока не зарегистрируемся!
        self.buttonSend.setEnabled(False)
        self.editTextMessage.setEnabled(False)
        self.editTextName.setEnabled(False)
        self.buttonEntry.setEnabled(False)
        # make onClickListeners:
        self.buttonConnect.pressed.connect(self.connect_to_server)
        self.buttonEntry.pressed.connect(self.reg_user)
        self.buttonSend.pressed.connect(self.send_message)
        self.buttonExit.pressed.connect(self.on_click_exit)
        # сделаем параметр, он будет создан один раз при инициализации на одно окно, пока не закроем
        self.after = 0 # параметр для времени сообщений (после какого времени загружать новые)
        self.url_address = "http://127.0.0.1:5000/"
        # делаем фоновый процесс обновления ленты сообщений:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_messages)

    def load_messages(self):
        try:
            data = requests.get(self.url_address + '/messages', params={utilies.AFTER_KEY: self.after}).json()
            for item in data[utilies.MESSAGES_KEY]:
                self.print_message(item)
                self.after = item[utilies.TIME_KEY]
        except:
            self.textViewMessages.setText("Server was fallen!")
            self.after = 0
            return

    def connect_to_server(self):
        self.url_address = self.editTextUrl.text()
        try:
            status = requests.get(self.url_address + '/connection').json()
            if status[utilies.STATUS_KEY] == utilies.STATUS_OK:
                # open next fields for registration
                self.editTextUrl.setEnabled(False)
                self.buttonConnect.setEnabled(False)
                self.buttonEntry.setEnabled(True)
                self.editTextName.setEnabled(True)
        except:
            self.editTextUrl.setText("")
            self.textViewMessages.setText("Неверный url!")
            return

    def on_click_exit(self):
        user_name = self.editTextName.text()
        user_name_json = {
            utilies.USER_NAME_KEY: user_name
        }
        try:
            requests.post(self.url_address + '/exit_user', json=user_name_json)
        except:
            self.textViewMessages.append("Problems!\n")
        exit()
        return

    def reg_user(self):
        # take vars from fields and make json var user_name_json for pushing on server
        user_name = self.editTextName.text()
        user_name_json = {
            utilies.USER_NAME_KEY: user_name
        }
        # now we are sending request to server and get some answer from it
        try:
            answer = requests.get(self.url_address + '/reg', params=user_name_json).json()
            if answer[utilies.IS_SUCH_USER_ON_SERVER_KEY]:
                self.textViewMessages.append("Такой пользователь уже есть в этом чате!\n")
                return
        except:
            print("Error")
            self.textViewMessages.append("Some Problems\n")
            return

        # button of entry and lineEditField for name we make unable
        self.buttonEntry.setEnabled(False)
        self.editTextName.setEnabled(False)
        # and button send and the field for messages we should make enable:
        self.editTextMessage.setEnabled(True)
        self.buttonSend.setEnabled(True)
        self.textViewMessages.setText('')
        self.textViewMessages.repaint()
        # запускаем наш таймер, то есть фоновую програмку для подгрузки сообщений
        self.timer.start(1000)

    def send_message(self):
        userName = self.editTextName.text()
        user_name_json = {
            utilies.USER_NAME_KEY: userName
        }
        text = self.editTextMessage.toPlainText()
        if text == 'exit()':
            try:
                requests.post(self.url_address + '/exit_user', json=user_name_json)
                exit()
                return
            except:
                self.textViewMessages.append("Error\n")
                return
        elif text != "":
            try:
                data = {utilies.USER_NAME_KEY: userName, utilies.TEXT_KEY: text}
                status = requests.get(self.url_address + '/send', json=data).json()
                print(status[utilies.RESULT_KEY])
                if status[utilies.RESULT_KEY] == 'ERROR':
                    print("Upload the program!")
                print()
            except:
                self.textViewMessages.append("problems in sending message\n")
                return
        self.editTextMessage.setText('')

    def print_message(self, mess):
        cur_time = datetime.fromtimestamp(mess[utilies.TIME_KEY]).strftime('%H:%M:%S---%Y/%m/%d')
        # print(mess['userName'], cur_time)
        # print(mess['text'])
        # print()
        self.textViewMessages.append(mess[utilies.USER_NAME_KEY])
        self.textViewMessages.append(cur_time)
        self.textViewMessages.append(mess[utilies.TEXT_KEY])
        self.textViewMessages.append('\n')
        self.textViewMessages.repaint()


# Запускаем окно и приложение в нем
app = QtWidgets.QApplication([])
window = WindowMessenger()
window.show()
app.exec_()
