# Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
# финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
# имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
# Оплата, Аванс, Вид расходов, Сумма расходов.

import sqlite3 as sq
from data_users import info_users

with sq.connect('expense_items.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS expences")
    cur.execute("""CREATE TABLE IF NOT EXISTS expences (
    order_number INTEGER PRIMARY KEY,
    last_name TEXT,
    place_trip TEXT,
    payment REAL,
    advance REAL,
    expence_type TEXT,
    expence_amount REAL
    )""")

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO expences VALUES(?, ?, ?, ?, ?, ?, ?)", info_users)


    # Поиск данных sql-запрос 1
    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM expences WHERE place_trip == "Ростов-на-Дону"')
        result_1 = cur.fetchall()
        print(result_1)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM expences WHERE last_name LIKE  "Б%"')
        result_2 = cur.fetchall()
        print(result_2)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM expences WHERE expence_type = "Питание"')
        result_3 = cur.fetchall()
        print(result_3)

    # sql - 2
    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE expences SET expence_type='Еда' WHERE expence_type=='Питание'")
        cur.execute("SELECT * FROM expences")
        result_4 = cur.fetchall()
        print(result_4)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE expences SET place_trip='Ростов-на-Дону' WHERE place_trip!='Ростов-на-Дону'")
        cur.execute("SELECT * FROM expences")
        result_5 = cur.fetchall()
        print(result_5)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE expences SET payment = payment+5000 WHERE order_number = 2")
        cur.execute("SELECT * FROM expences WHERE order_number = 2")
        result_6 = cur.fetchall()
        print(result_6)

    # sql - 3
    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expences WHERE order_number == 1")
        cur.execute("SELECT * FROM expences")
        result_7 = cur.fetchall()
        print(result_7)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expences WHERE order_number == 1")
        cur.execute("SELECT * FROM expences")
        result_7 = cur.fetchall()
        print(result_7)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expences WHERE last_name LIKE 'Б%'")
        cur.execute("SELECT * FROM expences")
        result_8 = cur.fetchall()
        print(result_8)

    with sq.connect('expense_items.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expences WHERE expence_type = 'Транспорт'")
        cur.execute("SELECT * FROM expences")
        result_9 = cur.fetchall()
        print(result_9)

