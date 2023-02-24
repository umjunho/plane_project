#SQLite 사용

import sqlite3
import os

print(sqlite3.version)
print(sqlite3.sqlite_version)
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '\\table.db')
cur = conn.cursor()

def make_table():
    #user table / primary key는 user_id
    cur.execute('''
    create table if not exists user(
        user_id TEXT not null,
        user_pw TEXT not null,
        user_name TEXT not null, 
        user_tel integer not null, 
        user_jumin integer not null,
        user_email TEXT,
        user_grade integer, 
        primary key(user_id)
        )
    ''')

    #airplane table / primary key는 air_name
    cur.execute('''
    create table if not exists airplane(
        air_name TEXT not null,
        capacity integer,
        primary key(air_name)
        )
    ''')

    #seat table
    cur.execute('''
    create table if not exists seat(
        seat_code TEXT not null,
        seat_price integer,
        air_name TEXT not null
        )
    ''')

    #timetable table / primary key는 time_num / foreign key는 air_name
    cur.execute('''
    create table if not exists timetable(
        time_num integer not null,
        loc_start TEXT,
        loc_des TEXT,
        time_start TEXT,
        time_des TEXT,
        air_name TEXT not null,
        primary key(time_num),
        foreign key(air_name) references airplane(air_name)
        )
    ''')

    #reservation table / primary key(res_num), foreign key는 user_id, time_num, air_name
    cur.execute('''
    create table if not exists reservation(
        res_num TEXT not null,
        user_id TEXT not null, 
        seat_code TEXT not null,
        time_num integer not null,
        air_name TEXT not null,
        primary key(res_num),
        foreign key(user_id) references user(user_id)
        foreign key(time_num) references timetable(time_num)
        foreign key(air_name) references airplane(air_name)
        )
    ''')

    #manager table/ primary key는 manager_id
    cur.execute('''
    create table if not exists manager(
        manager_id TEXT not null,
        manager_pw TEXT not null,
        primary key(manager_id)
        )
    ''')

def insert_data():

    #user set

    # user_id
    # user_pw 
    # user_name 
    # user_tel = 3자리 숫자 + '-' + 4자리 숫자 + '-' + 4자리 숫자 
    # user_jumin = 6자리 숫자 + '-' + 7자리 숫자
    # user_email = '@' + '.'
    # user_grade

    cur.execute('''
insert into user values('id_1', 'pw_1', '홍길동', '010-1234-5678', '800101-1234567', "hong@naver.com", 10)
''')
    
    #airplan set

    # air_name 
    # capacity 

    cur.execute('''
insert into airplane values('LJ101', 198)
''') 
    



    #seat set

    # seat_code = 열 (A,B,C,D,E,F) + 행
    # seat_price 
    # air_name 
    
#     cur.execute('''
# insert into seat values('A01', 198, 'LJ101')
# ''') 






    #timetable set

    # time_num = 년도 2자리 + 월 + 일 + 출발시간
    # loc_start 
    # loc_des
    # time_start = 시 : 분
    # time_des = 시 : 분
    # air_name 

    cur.execute('''
insert into timetable values(2302211230, 'SEOUL', 'JEJU', '12:30', '13:20', 'LJ101')
''') 

    #Reservation  set

    # res_num  = air_name + seat_code + time_num
    # user_id 
    # seat_code = 열 (A,B,C,D,E,F) + 행
    # time_num = 년도 2자리 + 월 + 일 + 출발시간
    # air_name 

    cur.execute('''
insert into reservation values('LJ101_A01_2302211230', 'id_1','A01', 2302211230,'LJ101')
''') 


make_table()
insert_data()

conn.commit()
conn.close()
