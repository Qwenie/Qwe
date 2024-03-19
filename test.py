import sqlite3  # библиотека для работы с базой данных
import csv  # работа с csv документами


with open('expenses.csv', newline='\n') as csvfile:  # читаем csv
    expenses = csv.reader(csvfile, delimiter=',')
    expenses = list(expenses)  # создаем список значений в питоновский list
    title_expenses = expenses[0]  # сохраняем название столбцов
    main_expenses = expenses[1:]  # сохраняем основные данные


con = sqlite3.connect("test.db")  # подключаемся в базе данных
cur = con.cursor()  # устанавливаем курсор
cur.execute("CREATE TABLE expenses(dt, Channel, costs)")  # создаем таблицу в бд
cur.executemany("INSERT INTO expenses VALUES (?, ?, ?)", main_expenses)  # вставляем данные в таблицу
con.commit()  # подтверждаем изменения в бд