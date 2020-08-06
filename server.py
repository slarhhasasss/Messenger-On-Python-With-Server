# Это приложение - наш сервер.


from flask import Flask, request, Response
import datetime
import time
import utilies

# Название нашего приложения
app = Flask(__name__)

# Это наши маленькие базы данных: бд сообщений и пользователей
messages = []
users_in_server = []


# Коорневой элемент. Возвращает html-страницу с сылкой на страницу статус
@app.route("/")
def hello():
    return "<a href='/status'> Статус </a>" \
           "<a href='/messages'> Messages </a>"


@app.route("/connection")
def connect_to_server():
    return {
        utilies.STATUS_KEY: utilies.STATUS_OK
    }


# Страница с статусом сервера
@app.route("/status")
def status():
    # Узнаем время на сервере
    cur_time = datetime.datetime.now()
    # возвращаем json файл:
    return {
        "Current time on server": cur_time,
        "Current amount of users:": len(users_in_server),
        "Current amount of messages:": len(messages)
    }


# Это метод, который не будет отображаться в браузере, чисто для запросов к нему
@app.route("/send")
def send():
    name = request.json[utilies.USER_NAME_KEY]  # вернет ошибку, если такого ключа нет
    if not (name in users_in_server):
        return {
            utilies.RESULT_KEY: "ERROR"
        }
    text = request.json.get(utilies.TEXT_KEY)  # вернет None, если такого ключа нет
    # if not name or isinstance(name, str) or not text or isinstance(text, str):
    #    return Response(status=400)
    message = {utilies.USER_NAME_KEY: name, utilies.TEXT_KEY: text, utilies.TIME_KEY: time.time()}
    # users_in_server.append(name)
    messages.append(message)
    # print(message)
    # print('\n')
    return {
        utilies.RESULT_KEY: "OK"
    }


# этот метод выполняется, когда пользователь покидает чат
@app.route("/exit_user", methods=['POST'])
def exit_user():
    # В запросе передается имя пользователя, по этому имени мы и удаляем его из онлайна
    cur_user_name = request.json.get(utilies.USER_NAME_KEY)
    try:
        users_in_server.remove(cur_user_name)
    except:
        return Response(status=400)
    return Response(status=200)


# этот метод тоже недоступен из браузера, т. к. если мы захотим обратиться к нему, то вылетит ошибка 400
@app.route("/reg")
def reg_user():
    try:
        # перед этим мы опять передали серверу некоторый json файл
        cur_user_name = str(request.args[utilies.USER_NAME_KEY])
    except:
        return {utilies.IS_SUCH_USER_ON_SERVER_KEY: True}
    # если такой пользователь уже есть на сервере, товозвращается True.
    if cur_user_name in users_in_server:
        print("such name is already on server!")
        return {utilies.IS_SUCH_USER_ON_SERVER_KEY: True}
    # если нет, то добавляем пользователя и возвращаем False
    users_in_server.append(cur_user_name)
    return {utilies.IS_SUCH_USER_ON_SERVER_KEY: False}


# страница видна в браузере и возвращает список сообщений
@app.route("/messages")
def messages_view():
    try:
        after = float(request.args[utilies.AFTER_KEY])
    except:
        return {utilies.MESSAGES_KEY: messages}
    filtered_messages = utilies.filter_by_key(messages, key=utilies.TIME_KEY, threshold=after)
    return {utilies.MESSAGES_KEY: filtered_messages}


if __name__ == "__main__":
    app.run()
