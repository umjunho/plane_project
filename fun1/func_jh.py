import sqlite3
import os
import re
path = os.path.dirname(__file__)
# conn = sqlite3.connect(path+'/user.db')
# cur = conn.cursor()


def login_user():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    user_id = input('ID를 입력해주세요 >>')
    user_pw = input(f'''{user_id} 비밀번호 >>''')
    test = 0
    sql = 'select * from user where user_id = ? and user_pw =?'
    try:
        cur.execute(sql, (user_id, user_pw))
        item = cur.fetchone()
        print(item[2]+'님 로그인 성공')
        test = 1
    except Exception as e:
        print('다시 입력해주세요.')
    conn.close()
    return test


def dup_user(user_id):
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    user_id = user_id
    sql = 'select count(*) from user where user_id = ?'
    cur.execute(sql, (user_id,))
    check = cur.fetchone()
    # print(check)
    return check


def join_user():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    user_id = input('아이디를 입력하세요 >>>')

    while True:
        test = dup_user(user_id)
        if test[0] >= 1:
            print('중복된 ID 입니다.')
            user_id = input('아이디를 입력하세요 >>>')
        else:
            break
    user_pw = input('비밀번호를 입력하세요 >>>')
    user_name = input('이름을 입력하세요 >>>')
   
    
    while True:
        check = None
        user_tel = input('전화번호를 입력하세요 >>>')
        if check == None:
            p = re.compile('[0-9]{,3}[-][0-9]{4}[-][0-9]{4}')
            if p.search(user_tel) != None:
                break
            else:
                print('전화번호 형식이 다릅니다.')

    while True:
        check = None
        user_jumin = input('주민번호를 입력하세요 >>>')
        if check == None:
            p = re.compile('[0-9]{6}[-][0-9]{7}')
            if p.search(user_jumin) != None:
                break
            else:
                print('-를 포함한 정확한 주민등록 번호를 입력하세요')
    
   
    while True:
        check = None
        user_email = input('이메일을 입력하세요 >>>')
        if check == None:
            p = re.compile('[\S]@[a-z]{2,}[.][a-z]{3}')
            if p.search(user_email) != None:
                break
            else:
                print('이메일 형식이 다릅니다.')

    sql = 'insert into user(user_id,user_pw,user_name,user_tel,user_jumin,user_email) values(?,?,?,?,?,?)'
    
    cur.execute(sql, (user_id, user_pw, user_name,
                user_tel, user_jumin, user_email))
    conn.commit()
    conn.close()


def loc_start():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    
    sql = 'select distinct(loc_start) from timetable'
    cur.execute(sql)
    list = []
    for item in cur.fetchall():
        list.append(item[0])
    print(list)
    conn.close()

    return  list


def loc_depart():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    sql = 'select distinct(loc_des) from timetable'
    
    cur.execute(sql)
    list = []
    for item in cur.fetchall():
        list.append(item[0])
    # print(list)
    conn.close()

    return  list