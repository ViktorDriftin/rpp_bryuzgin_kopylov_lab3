# Копылов Кирилл, Брюзгин Виктор ФБИ-02
# Лабораторная работа №3
# Вариант 6

# --------------------------------------------------------------------------------------------
# Импортируем модуль http.client для создания HTTP-запросов
import http.client
# Импортируем модуль json для работы с данными в формате JSON
import json

# Определяем функцию operate, которая принимает два аргумента: строку в формате JSON data и целое число left
def operate(data: str, left: int):

    # Преобразуем данные в формате JSON из строки data в словарь Python с помощью функции json.loads()
    dict = json.loads(data)

    # Если операция равна 'mul' (умножение), то умножаем left на число из словаря и возвращаем результат
    if dict['operation'] == 'mul':
        return left * dict['number']

    # Если операция равна 'sub' (вычитание), то вычитаем число из словаря из left и возвращаем результат
    if dict['operation'] == 'sub':
        return left - dict['number']

    # Если операция равна 'div' (деление), то делим left на число из словаря и возвращаем результат
    if dict['operation'] == 'div':
        return left / dict['number']

    # Если операция равна 'sum' (сложение), то складываем left с числом из словаря и возвращаем результат
    if dict['operation'] == 'sum':
        return left + dict['number']

# --------------------------------------------------------------------------------------------
# Задание 1: Отправить HTTP запрос GET /number/{Вариант}.

# Устанавливаем соединение с веб-сервером по адресу 167.172.172.227 и порту 8000 через протокол HTTP
connect = http.client.HTTPConnection("167.172.172.227:8000")
# Отправляем GET-запрос на сервер с указанием пути /number/6
connect.request ("GET", "/number/6")
# Получаем ответ от сервера и сохраняем его в переменной response1
response1 = connect.getresponse()
# Выводим на экран статус ответа и его причину
print(response1.status, response1.reason)
# Декодируем тело ответа из байтовой строки в строку типа str
decoded_body = response1.read().decode()
# Преобразуем строку JSON в объект Python типа dict и извлекаем значение поля number
left = json.loads(decoded_body)['number']
# Выводим на экран значение переменной left
print(left)

# --------------------------------------------------------------------------------------------
# Задание 2: Отправить HTTP запрос GET /number/ с параметром запроса option={Вариант}
# Устанавливаем соединение с веб-сервером по адресу 167.172.172.227 и порту 8000 через протокол HTTP
connect = http.client.HTTPConnection("167.172.172.227:8000")
# Отправляем GET-запрос на сервер с указанием пути /number/6
connect.request('GET', '/number/?option=6')
# Получение ответа от сервера
response1 = connect.getresponse()
# Вывод статуса ответа (код состояния HTTP) и причины (строковое описание кода состояния)
print(response1.status, response1.reason)
# Декодирование тела ответа сервера в строку и передача этой строки в функцию "operate" вместе с переменной "left", затем сохранение результата в переменной "left"
decoded_body = response1.read().decode()
# Вызов функции operate с параметрами decoded_body и left, сохранение результата в переменной left
left = int(operate(decoded_body, left))
# Вывод значения переменной left
print(left)

# --------------------------------------------------------------------------------------------
# Задание 3: Отправить HTTP запрос POST /number/ с телом option={Вариант}.
# Устанавливаем соединение с веб-сервером по адресу 167.172.172.227 и порту 8000 через протокол HTTP
connect = http.client.HTTPConnection("167.172.172.227:8000")
# Создание заголовков запроса с указанием формата данных в теле запроса
headers = {'Content-type': 'application/x-www-form-urlencoded'}
# Отправка POST-запроса на сервер по указанному адресу "/number/" с параметром "option=6" и заголовками из переменной "headers"
connect.request('POST', '/number/', 'option=6', headers)
# Получение ответа от сервера
response1 = connect.getresponse()
# Вывод статус-кода и причины ответа сервера
print(response1.status, response1.reason)
# Декодирование тела ответа сервера в строку и передача этой строки в функцию "operate" вместе с переменной "left", затем сохранение результата в переменной "left"
decoded_body = response1.read().decode()
# Вызов функции operate с параметрами decoded_body и left, сохранение результата в переменной left
left = int(operate(decoded_body, left))
# Вывод значения переменной left
print(left)

# --------------------------------------------------------------------------------------------
# Задание 4: Отправить HTTP запрос PUT /number/ с телом JSON {"option": {Вариант}}.
# Устанавливаем соединение с веб-сервером по адресу 167.172.172.227 и порту 8000 через протокол HTTP
connect = http.client.HTTPConnection("167.172.172.227:8000")
# Задание заголовков запроса для отправки в формате JSON
headers = {'Content-type': 'application/json'}
# Отправка PUT-запроса по указанному пути с передачей тела запроса в формате JSON и заголовков
connect.request('PUT', '/number/', json.dumps({'option': 6}), headers)
# Получение ответа от сервера
response1 = connect.getresponse()
# Вывод статус-кода и причины ответа сервера
print(response1.status, response1.reason)
# Декодирование тела ответа сервера в строку и передача этой строки в функцию "operate" вместе с переменной "left", затем сохранение результата в переменной "left"
decoded_body = response1.read().decode()
# Вызов функции operate с параметрами decoded_body и left, сохранение результата в переменной left
left = int(operate(decoded_body, left))
# Вывод результата работы функции operate()
print(left)

# --------------------------------------------------------------------------------------------
# Задание 5: Отправить HTTP запрос DELETE /number/ с телом JSON {"option": {Вариант}}.
# Устанавливаем соединение с веб-сервером по адресу 167.172.172.227 и порту 8000 через протокол HTTP
connect = http.client.HTTPConnection("167.172.172.227:8000")
# Отправка DELETE-запроса по указанному пути с передачей тела запроса в формате JSON
connect.request('DELETE', '/number/', json.dumps({'option': 6}))
# Получение ответа от сервера
response1 = connect.getresponse()
# Вывод статус-кода и причины ответа сервера
print(response1.status, response1.reason)
# Декодирование тела ответа сервера в строку и передача этой строки в функцию "operate" вместе с переменной "left", затем сохранение результата в переменной "left"
decoded_body = response1.read().decode()
# Вызов функции operate с параметрами decoded_body и left, сохранение результата в переменной left
left = int(operate(decoded_body, left))
# Вывод результата работы функции operate()
print(left)