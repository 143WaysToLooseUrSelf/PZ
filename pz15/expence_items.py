import sqlite3 as sq
from data_users import info_users

with sq.connect('expense_items.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS expences")
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
        cur.executemany("INSERT INTO expences VALUES (?, ?, ?, ?, ?, ?, ?)", info_users)
        cur.execute("SELECT * FROM expences")
        result = cur.fetchall()
        print(result)

    # # Поиск данных sql-запрос 1
    # with sq.connect('expense_items.db') as con:
    #     cur = con.cursor()
    #     cur.execute('SELECT * FROM expences WHERE order_number = 5')
    #     result = cur.fetchall()
    #     print(result)

    # Поиск данных sql-запрос 2
    # with sq.connect('expense_items.db') as con:
    #     cur = con.cursor()
    #     cur.execute('SELECT * FROM expences WHERE order_number BETWEEN 500 AND 10000')
    #     result = cur.fetchall()
    #     print(result)

    # with sq.connect('expense_items.db') as con:
    #     cur = con.cursor()
    #     cur.execute('UPDATE expences SET payment = payment+1000 WHERE order_number = 2')
    #     result = cur.fetchall()
    #     print(result)