import sqlite3  # библиотека для работы с базой данных
import csv  # работа с csv документами


con = sqlite3.connect("test.db")  # подключаемся в базе данных
cur = con.cursor()  # устанавливаем курсор
download_expenses = cur.execute("SELECT * FROM expenses").fetchall()  # получаем все данные из таблицы в виде списка


with open('download_expenses.csv', 'w', newline='', encoding='utf-8') as f:  # создаем документ на запись
    write = csv.writer(f)  # создаем объект writer
    write.writerow(['dt', 'Channel', 'costs'])  # записываем название столбцов
    write.writerows(download_expenses)  # пишем остальные данные из списка значений
