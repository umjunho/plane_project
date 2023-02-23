import sqlite3
import os

print(sqlite3.version)
print(sqlite3.sqlite_version)
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '\\table.db')
cur = conn.cursor()

def insert_data():

    #user set
    try:
        sql_user = 'insert into user values(?,?,?,?,?,?,?)'

        data_user = [
            ('id_2', 'pw_2', '엄준호', '010-4535-3424', '973489-1234567', "jun@naver.com", 5),
            ('id_3', 'pw_3', '이가영', '010-6735-3422', '991117-2234567', "ga@naver.com", 3),
            ('id_4', 'pw_4', '양수빈', '010-6755-2623', '983402-2234567', "jang@naver.com", 7),
            ('id_5', 'pw_5', '송민규', '010-8923-8736', '963489-1234567', "song@naver.com", 2),
            ('id_6', 'pw_6', '김철수', '010-1239-5453', '603984-1234567', "kim@naver.com", 1),
            ('id_7', 'pw_7', '김영희', '010-6425-8763', '603934-2234567', "kimyueng@naver.com", 6),
            ('id_8', 'pw_8', '콩쥐', '010-8624-4567', '4058748-2234567', "kong@naver.com", 1)]
        
        cur.executemany(sql_user, data_user)
    except:
        pass



    #airplan set
    try:
        sql_airplan = 'insert into airplane values(?,?)'

        data_airplan = [
            ('LJ102', 198),
            ('LJ201', 198),
            ('LJ202', 198),
            ('SM101', 30),
            ('SM102', 30),
            ('SM201', 30),
            ('SM202', 30)]
        
        cur.executemany(sql_airplan, data_airplan)
    except:
        pass



    #seat set seatcode를 primary key로하면 문제
    try:
        sql_seat = 'insert into seat values(?,?, ?)'

        data_seat = []
        for i in range(1, 34):
            num = 'A' + str(i)
            data_seat.append((num, 20000, 'LJ101'))
            num = 'B' + str(i)
            data_seat.append((num, 20000, 'LJ101'))
            num = 'C' + str(i)
            data_seat.append((num, 20000, 'LJ101'))
            num = 'D' + str(i)
            data_seat.append((num, 20000, 'LJ101'))
            num = 'E' + str(i)
            data_seat.append((num, 20000, 'LJ101'))
            num = 'F' + str(i)
            data_seat.append((num, 20000, 'LJ101'))

        for i in range(1, 34):
            num = 'A' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
            num = 'B' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
            num = 'C' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
            num = 'D' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
            num = 'E' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
            num = 'F' + str(i)
            data_seat.append((num, 20000, 'LJ102'))
        
        for i in range(1, 34):
            num = 'A' + str(i)
            data_seat.append((num, 20000, 'LJ201'))
            num = 'B' + str(i)
            data_seat.append((num, 20000, 'LJ201'))
            num = 'C' + str(i)
            data_seat.append((num, 20000, 'LJ201'))
            num = 'D' + str(i)
            data_seat.append((num, 20000, 'LJ201'))
            num = 'E' + str(i)
            data_seat.append((num, 20000, 'LJ201'))
            num = 'F' + str(i)
            data_seat.append((num, 20000, 'LJ201'))

        for i in range(1, 34):
            num = 'A' + str(i)
            data_seat.append((num, 20000, 'LJ202'))
            num = 'B' + str(i)
            data_seat.append((num, 20000, 'LJ202'))
            num = 'C' + str(i)
            data_seat.append((num, 20000, 'LJ202'))
            num = 'D' + str(i)
            data_seat.append((num, 20000, 'LJ202'))
            num = 'E' + str(i)
            data_seat.append((num, 20000, 'LJ202'))
            num = 'F' + str(i)
            data_seat.append((num, 20000, 'LJ202'))

        for i in range(1, 6):
            num = 'A' + str(i)
            data_seat.append((num, 15000, 'SM101'))
            num = 'B' + str(i)
            data_seat.append((num, 15000, 'SM101'))
            num = 'C' + str(i)
            data_seat.append((num, 15000, 'SM101'))
            num = 'D' + str(i)
            data_seat.append((num, 15000, 'SM101'))
            num = 'E' + str(i)
            data_seat.append((num, 15000, 'SM101'))
            num = 'F' + str(i)
            data_seat.append((num, 15000, 'SM101'))

        for i in range(1, 6):
            num = 'A' + str(i)
            data_seat.append((num, 15000, 'SM102'))
            num = 'B' + str(i)
            data_seat.append((num, 15000, 'SM102'))
            num = 'C' + str(i)
            data_seat.append((num, 15000, 'SM102'))
            num = 'D' + str(i)
            data_seat.append((num, 15000, 'SM102'))
            num = 'E' + str(i)
            data_seat.append((num, 15000, 'SM102'))
            num = 'F' + str(i)
            data_seat.append((num, 15000, 'SM102'))

        for i in range(1, 6):
            num = 'A' + str(i)
            data_seat.append((num, 15000, 'SM201'))
            num = 'B' + str(i)
            data_seat.append((num, 15000, 'SM201'))
            num = 'C' + str(i)
            data_seat.append((num, 15000, 'SM201'))
            num = 'D' + str(i)
            data_seat.append((num, 15000, 'SM201'))
            num = 'E' + str(i)
            data_seat.append((num, 15000, 'SM201'))
            num = 'F' + str(i)
            data_seat.append((num, 15000, 'SM201'))

        for i in range(1, 6):
            num = 'A' + str(i)
            data_seat.append((num, 15000, 'SM202'))
            num = 'B' + str(i)
            data_seat.append((num, 15000, 'SM202'))
            num = 'C' + str(i)
            data_seat.append((num, 15000, 'SM202'))
            num = 'D' + str(i)
            data_seat.append((num, 15000, 'SM202'))
            num = 'E' + str(i)
            data_seat.append((num, 15000, 'SM202'))
            num = 'F' + str(i)
            data_seat.append((num, 15000, 'SM202'))
        
        cur.executemany(sql_seat, data_seat)
    except:
        pass



#     #timetable set
    try:
        sql_timetable = 'insert into timetable values(?,?,?,?,?,?)'

        data_timetable = [
            (2302211530, 'JEJU', 'SEOUL', '15:30', '16:20', 'LJ101'),
            (2302211000, 'SEOUL', 'JEJU', '10:00', '10:50', 'LJ102'),
            (2302211300, 'JEJU', 'SEOUL', '13:00', '13:50', 'LJ102'),
            (2302211630, 'SEOUL', 'JEJU', '16:30', '17:20', 'LJ201'),
            (2302212030, 'JEJU', 'SEOUL', '20:30', '21:20', 'LJ201'),
            (2302211800, 'SEOUL', 'JEJU', '18:00', '18:50', 'LJ202'),
            (2302212200, 'JEJU', 'SEOUL', '22:00', '22:50', 'LJ202')
            ]
        
        cur.executemany(sql_timetable, data_timetable)
    except:
        pass


#     #Reservation  set
    try:
        sql_reservation = 'insert into reservation values(?,?,?,?,?)'

        data_reservation = [
            ('LJ201_D15_2302211630', 'id_5', 'D15', 2302211630, 'LJ201'),
            ('LJ202_C4_2302211800', 'id_3', 'C4', 2302211800, 'LJ202'),
            ('LJ102_F10_2302211300', 'id_8', 'F10', 2302211300, 'LJ102'),
            ('LJ201__2302211630', 'id_4', 'A2', 2302211630, 'LJ201'),
            ('LJ201_B24_2302212030', 'id_1', 'B24', 2302212030, 'LJ201'),
            ]
        
        cur.executemany(sql_reservation, data_reservation)
    except:
        pass

insert_data()

conn.commit()
conn.close()
