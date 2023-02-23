import sqlite3
import os
import re
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/table.db')
cur = conn.cursor()


def dup_id():
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    while True:
        id = input()
        sql = 'select * from user where user_id=? '
        cur.execute(sql,(id,))
        user_id=cur.fetchone()
        if user_id==None:
            break
        else:
            print('중복된 아이디 입니다')



            


    # for i in bin:
    #     if i == id:
    #         print('중복된 아이디 입니다 ')

        #  if item==id:
        #       print('다시입력해 주세요')



def login():

    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    try:
        while True:
            sql = 'select * from user where user_id=? and user_pw=?'
            id = input("아이디")
            pass_word = input('비밀번호')
            cur.execute(sql, (id, pass_word))
            us = cur.fetchone()
            if us!=None:
                print('환영합니다')
                break

            else:
                print('다시입력 해주세요')

    except Exception as e:
        print(e)


    # try:
    #     sql = 'select * from user where user_id=? and user_pw=?'
    #     id = input("아이디")
    #     pass_word = input('비밀번호')

    #     cur.execute(sql, (id, pass_word,))

    #     print('환영합니다 ')
    # except Exception as e:
    #     print(e)



def member():
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    try:

        sql = 'insert into user(user_id,user_pw,user_name,user_tel,user_jumin,user_email) values(?,?,?,?,?,?)'
        dup_id


        name = input('이름')
        while True:

            tell = input('전화번호')
            p = re.compile('[0-1]{3}[-][0-9]{4}[-][0-9]{4}')
            result = p.search(tell)
            if result != None:

                break
            else:
                print('다시입력해 주세요')

        while True:

            user_number = input('주민번호')
            p = re.compile('[0-9]{6}[-][1-4]{1}[0-9]{6}')
            result = p.search(user_number)
            if result != None:
                break
            else:
                print('다시 입력해 주세요')
        while True:

            email = input('이메일')
            p = re.compile('@[a-z]{2,}[.][a-z]{,3}')
            result = p.search(email)
            if result != None:
                break
            else:
                print('다시입력해 주세요')
        pass_word = input('비밀번호')

        cur.execute(sql, (id, name, tell, user_number, email, pass_word))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def ticketing():
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    try:
        #로그인 
        sql = 'select * from timetable where loc_start=? and loc_des=?'
        starting_point = input("출발지").upper()
        end_point= input('도착지').upper()
        i=1
        cur.execute(sql, (starting_point,end_point))
        item_list= [(),] ## 1부터 출력 되도록 
        for item in cur.fetchall():
            print(i,end=' ')

            print(item)
            i=i+1
            item_list.append(item)
        
        i= int(input('원하는 시간을  번호로 입력해 주세요 :'))
        # print(item_list[i])
        
        
        print(item_list[i])

        return item_list[i]
           
        # sql_1 = 'select *from timetable where loc_start=? and loc_des=? and time_start=?'
        # start_time= input('출발 시간을 입력해 주세요')
        # cur.execute(sql_1,(starting_point,end_point,start_time))
        # us = cur.fetchone()
        # print(us)

        # #좌석 선택 
    
    except Exception as e:
        print(e)
    conn.close()






