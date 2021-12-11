import csv
import os
import sqlite3

DB_FILENAME = 'Traffic_Accident.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS accident;")
cur.execute("""CREATE TABLE accident(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "월" VARCHAR(10),
    "요일" VARCHAR(10),
    "발생지_시도" VARCHAR(100),
    "기상상태" VARCHAR(50),
    "하루_교통사고_건수합" INTEGER
            );""")


f = open('./교통사고데이터.csv', 'r',encoding='utf-8')
reader = csv.reader(f)
title = next(reader)

for id, line in enumerate(reader):
    cur.execute("""INSERT INTO accident(id, 월, 요일, 발생지_시도, 기상상태, 하루_교통사고_건수합)
                VALUES (?,?,?,?,?,?);
                """,(id+1, line[1], line[2],line[3], line[4], line[5])
    )

f.close()

conn.commit()
conn.close()