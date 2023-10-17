import os
import time

import requests

org = 'podk'
pc = 'serv'
prg = 'script'
msg = 'авария случилась'
msg = 'sdsd'
text = f'{org}   ||  {pc}  ||   {prg}   ||   {msg}'
#text = f'dsdd|| {org}{pc}{prg}'


mask = ['.trn','.bak']
#    (24*60*60) - Это день
srok = 80*(24*60*60) 
# удалять или нет пустые папки
delete_clear_folder = False
log='log.txt'
del_file = 0
all_file = 0

# Директория, в которой нужно удалять файлы
directory = 'c:\\BACKUP\\'

# Получаем текущую дату и время
current_time = time.time()
struct = time.localtime(current_time)
date = time.strftime('%d.%m.%Y %H:%M', struct)

# Функция для удаления файла
def delete_file(file_path):
    global del_file
    os.remove(file_path)
    del_file += 1
    #print(f'Файл {file_path} удален')

# Функция для удаления пустых папок
def delete_empty_folders(directory):
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        # Проверяем, является ли объект папкой
        if os.path.isdir(folder_path):
            # Если папка пустая, удаляем ее
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                print(f'Папка {folder_path} удалена')

# Рекурсивная функция для обхода директории и удаления старых файлов
def process_directory(directory):
    global all_file
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Проверяем, является ли объект файлом
        if os.path.isfile(file_path):
            all_file += 1
            #print(f'{file_path}')
            # Получаем время последнего изменения файла
            file_time = os.path.getmtime(file_path)
            # Если разница между текущим временем и временем изменения файла больше 10 дней в секундах (10 дней * 24 часа * 60 минут * 60 секунд)
            if (current_time - file_time) > srok:
                if os.path.splitext(file_path)[1] in mask:
                    delete_file(file_path)
        # Если объект является директорией, запускаем функции рекурсивно для этой директории
        elif os.path.isdir(file_path):
            process_directory(file_path)

    # Удаляем пустые папки после удаления файлов
    if delete_clear_folder: delete_empty_folders(directory)

# Запускаем функцию для указанной директории
process_directory(directory)
res_1 = f'Всего - {all_file}'
res_2 = f'Удалено - {del_file}'
print(res_1)
print(res_2)
with open(directory+log,'a') as file:
    file.write(f"Запуск - {date}\n")
    file.write(f"Всего - {all_file}\n")
    file.write(f"Удалено - {del_file}\n")

msg = 'sdsd'
text = f'{org}   ||  {pc}  ||   {prg}   ||   {msg}'
#text = f'dsdd|| {org}{pc}{prg}'
url = f'https://api.telegram.org/bot******bot key******/sendMessage?chat_id=999999999999999999999&parse_mode=Markdown&text={text}'
response = requests.get(url)
text = f'Запуск - {date}\nВсего - {all_file}\n Удалено - {del_file}\n'
#text = f'dsdd|| {org}{pc}{prg}'
url = f'https://api.telegram.org/bot******bot key******/sendMessage?chat_id=99999999999999999999999999&parse_mode=Markdown&text={text}'
response = requests.get(url)





