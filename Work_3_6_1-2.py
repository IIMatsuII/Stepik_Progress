'''

Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests
with open("C:/Users/vobuk/PycharmProjects/pythonProject/dataset_3378_2.txt") as file:
    s = file.readline().strip()
r = requests.get(s)
r = r.text
r = r.splitlines()
with open("C:/Users/vobuk/PycharmProjects/pythonProject/dataset_3378_2.txt", "w") as out:
    out.write(str(len(r)))
'''

'''
import requests
with open('C:/Users/vobuk/PycharmProjects/pythonProject/dataset_3378_3.txt') as file:
    s = file.readline().strip()
    r = requests.get(s)
while True:
    ss = 'https://stepic.org/media/attachments/course67/3.6.3/' + r.text
    r = requests.get(ss)
    if len(r.text) > 20:
        break

with open('C:/Users/vobuk/PycharmProjects/pythonProject/output.txt', 'w') as out:
    out.write(str(r.text))
'''