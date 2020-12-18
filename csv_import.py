import csv
import sqlite3
import os

def csv_parse(file_name):
    conn = sqlite3.connect('db.sqlite3')
    print ("Opened database successfully")
    # Naredi frišno
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count < 2:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                conn.execute(f"INSERT INTO vprasanja(vprasanje, odgovori, nepravilni)\
                    VALUES ( '{row[1]}', '{row[2]}', '{row[3]}' );")
                line_count += 1
    print(f'Processed {line_count} lines.')
    conn.commit()
    print ("Records created successfully")
    conn.close()

def create_table():
    os.remove("db.sqlite3")
    open('db.sqlite3', 'a').close()
    conn = sqlite3.connect('db.sqlite3')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS vprasanja
             (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
             vprasanje           TEXT    NOT NULL,
             odgovori            TEXT     NOT NULL,
             nepravilni        TEXT NOT NULL);''')
    print ("Table created successfully")
    conn.close()
create_table()
csv_parse('qna/vprasanja_in_odgovori.csv')

