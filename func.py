# 1.여정선택 2.항공편 선택 3. 탑승객 정보 4.결제




#       회원 만들기
# 1. 로그인 2.회원가입
#   if(1) - login_user
# 1.아이디 2.비번
#   if(2) - join_user
# 1.정보입력 ->로그인



#      예매 
# 1.출발지 2.도착지
# 1.편도, 2.왕복
# 1.시간표
# 1.좌석선택(포도알)

                                                                            #   if(왕복)
                                                                            # 1.시간표
                                                                            # 1.좌석선택(포도알)

#  예매 끝
# 1. 결제금액 2.시간및좌석확인






# 마일리지 넣어서 등급해서 할인

# 관리자 시간표, 비행기, 시트



# 회원이 예매취소, 탈퇴 (delet)





#        확인(로그인)
# 티켓확인 
# 회원정보확인 
#회원정보 수정





#로그아웃

# 종료


import sqlite3,os,re
import pandas as pd
path = os.path.dirname(__file__)
# conn = sqlite3.connect(path+'/user.db')
# cur = conn.cursor()


def login_user(): #로그인 함수
    conn = sqlite3.connect(path+'/table.db')
    id_pw = pd.read_sql_query("select user_id, user_pw from user", conn).values #.values > dataframe값을 리스트로 인덱스 없이 추출하는 코드
    check =0
    login = ""

    id_ox = input("                ID를 입력해주세요 >>")
    for i in range(len(id_pw)):
        if id_ox == id_pw[i][0]: #db에 user_id값이 있는지 확인하는 코드
            pw = input(f"""
                                    |로그인|
---------------------------------------------------------------------------------------------------
                ID: {id_ox}    패스워드 >>""")
            check = 1
            if pw == id_pw[i][1]:
                print("""                              로그인 완료!        """)
                login = id_pw[i][0]
            else:
                print("                 비밀번호가 올바르지않습니다.")
                
    if check == 0:
        print("                 일치하는 id가 존재하지 않습니다.")

    conn.close()
    return login


def dup_user(user_id): #id중복 확인 함수
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    user_id = user_id
    sql = 'select count(*) from user where user_id = ?'
    cur.execute(sql, (user_id,))
    check = cur.fetchone()
    # print(check)
    return check


def join_user(): #회원가입 함수
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()

    user_id = input('아이디를 입력하세요 >>>')
    while True:
        test = dup_user(user_id)
        if user_id=="":
            user_id = input('아이디를 입력하세요 >>>')
        elif test[0] >= 1:
            print('중복된 ID 입니다.')
            user_id = input('아이디를 입력하세요 >>>')
        else:
            break

        
    user_pw = input('비밀번호를 입력하세요 >>>')
               
    while True:
        if user_pw == "":
            user_pw = input('비밀번호를 입력하세요 >>>')
        else:
            break



    user_name = input('이름을 입력하세요 >>>')            
    while True:
        if user_name == "":
            user_name = input('이름을 입력하세요 >>>')
        else:
            break
    
    while True:
        check = None
        user_tel = input('전화번호를 입력하세요 >>>')
        if check == None:
            p = re.compile('[0-9]{2,3}[-][0-9]{4}[-][0-9]{4}') #형식에 맞지 않으면 값이 들어가지 않게 정규표현식, 숫자2~3자리-숫자 4자리-숫자 4자리
            if p.search(user_tel) != None:
                break
            else:
                print('전화번호 형식이 다릅니다.')

    while True:
        check = None
        user_jumin = input('주민번호를 입력하세요 >>>')
        if check == None:
            p = re.compile('[0-9]{6}[-][1-4]{1}[0-9]{6}') #정규표현식 숫자6자리-숫자(1~4성별)1자리 숫자6자리
            if p.search(user_jumin) != None:
                break
            else:
                print('-를 포함한 정확한 주민등록 번호를 입력하세요')
    
   
    while True:
        check = None
        user_email = input('이메일을 입력하세요 >>>')
        if check == None:
            p = re.compile('[\S]@[a-z]{2,}[.][a-z]{3}') # @앞에 공백 안됨, 문자2개이상.문자3자리
            if p.search(user_email) != None:
                break
            else:
                print('이메일 형식이 다릅니다.')

    sql = 'insert into user(user_id,user_pw,user_name,user_tel,user_jumin,user_email) values(?,?,?,?,?,?)'
    
    cur.execute(sql, (user_id, user_pw, user_name,
                user_tel, user_jumin, user_email))
    conn.commit()
    conn.close()
    return user_id


def check_ticket(login): #예매 정보를 출력하는 함수
    path = os.path.dirname(__file__)
    conn = sqlite3.connect(path + '\\table.db')
    ticket = pd.read_sql_query("select * from reservation", conn).values
    time = pd.read_sql_query("select * from timetable", conn).values
    check = 0

    print(f'{login}님의 티켓 현황입니다.')
    for i in range(len(ticket)):
        if ticket[i][1] == login:
            if check != 1:
                for j in range(len(time)):
                    if time[j][0] == ticket[i][3]:

                        print("""
---------------------------------------
sajo AIR     [탑승권]
---------------------------------------
     """)
                        print('티켓번호:',ticket[i][0],'\n좌석번호:',ticket[i][2],'\n비행기 기종:',ticket[i][4])
                        print('출발지:',time[j][1],'출발시간:',time[j][3],'\n도착지:',time[j][2],'도착시간:',time[j][4])
                        print('''---------------------------------------''')
    check = 1
    
    if check ==0:
        print("티켓이 없습니다.")


def check_info(login): #회원 정보 확인 함수
    path = os.path.dirname(__file__)
    conn = sqlite3.connect(path + '\\table.db')
    user = pd.read_sql_query("select * from user", conn).values 

    for i in range(len(user)):
        if user[i][0] ==login:
            print('이름:',user[i][2],'\n비밀번호:',user[i][1],'\n전화번호:',user[i][3],'\n주민등록번호:',user[i][3],'\n이메일:',user[i][5])

def update_userinfo(login): #회원정보 수정 함수 #주민등록번호는 수정 불가능하므로 넣지 않음
    path = os.path.dirname(__file__)
    conn = sqlite3.connect(path + '\\table.db')
    cur = conn.cursor()
    user = pd.read_sql_query("select * from user", conn).values 

    for i in range(len(user)):
        if user[i][0] ==login:
            check =1
            while check != 0:
                col = input("수정할 정보를 선택해주세요[user_pw,user_name,user_tel,user_email] >>")

                if col == "user_pw":
                    value = input('비밀번호를 입력하세요 >>>')
                    check = 0
                
                elif col == "user_name":
                    value = input('이름을 입력하세요 >>>')
                    check =0

                elif col == "user_tel": #정보 수정시 회원가입때와 같은 제약조건
                    value = input('전화번호를 입력하세요 >>>')
                    p = re.compile('[0-9]{2,3}[-][0-9]{4}[-][0-9]{4}')
                    if p.search(value) != None:
                        check=0
                        break
                    else:
                        print('전화번호 형식이 다릅니다.')

                elif col == "user_email": #정보 수정시 회원가입때와 같은 제약조건
                    value = input('이메일을 입력하세요 >>>')
                    p = re.compile('[\S]@[a-z]{2,}[.][a-z]{3}')
                    if p.search(value) != None:
                        check=0
                        break
                    else:
                        print('이메일 형식이 다릅니다.')
                else:
                    print("수정할 정보를 잘못 입력하셨습니다.")


            sql = f"update user set {col} = ? where user_id = ?" #update를 사용하여 수정된 값 집어넣음
            cur.execute(sql,(value,login))

    conn.commit() #값이 변경되었기 때문에 commit,close
    conn.close()

def ticketing(): # 원하는 출발지 도착지 선택에 맞는  비행 스케줄 선택  
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    try:
        
        sql = 'select * from timetable where loc_start=? and loc_des=? order by time_start'#입력받은 출발 도착지 출력 
        sql_2 = 'select distinct loc_start from timetable'#중복 제거한 출발지
        sql_3 = 'select distinct loc_des from timetable where loc_start =?'#중복 제거한 도착지 
        cur.execute(sql_2)
        start = ()
        print('''---------------------------------------------------------------------------------------------------''')
        print(f'''출발지 : ''', end=' ')
        for item in cur.execute(sql_2):
            print(f'''{item[0]}''', end=' ')
            start = start + item
        print()
        starting_point = input("출발지를 입력해 주세요 >>>").upper()
        if starting_point not in start:
            print('출발지를 잘못 입력하셨습니다.')
            return ""
        cur.execute(sql_3,(starting_point,))
        print('''---------------------------------------------------------------------------------------------------''')
        print(f'''도착지 : ''', end=' ')
        end = ()
        for item in cur.execute(sql_3,(starting_point,)):
            print(f'''{item[0]}''', end=' ')
            end = end + item
        print()
        end_point= input('도착지를 입력해 주세요 >>>').upper()
        if end_point not in end:
            print('도착지를 잘못 입력하셨습니다.')
            return ""
        i=1
        cur.execute(sql, (starting_point,end_point))
        item_list= [(),] ## 1부터 출력 되도록
        print('''---------------------------------------------------------------------------------------------------''') 
        for item in cur.fetchall():
            print(i,end=' ')## 1234 출력 
            print(f'''날짜: {item[0]}  출발지: {item[1]}  도착지: {item[2]}  출발 시간: {item[3]}  도착 시간: {item[4]} 비행기번호: {item[5]}''')
            # print(f'''출발 시간: {item[3]}  도착 시간: {item[4]}''')
            i=i+1
            item_list.append(item)
        
        print('''---------------------------------------------------------------------------------------------------''')
        i= int(input('원하는 시간을 번호로 입력해 주세요 :'))
        # print(item_list[i])
        
        conn.close()
        return item_list[i]

    except Exception as e:
        conn.close()
        print(e)
        return ""
    


def ticketing2(start, end):  #왕복-2
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    try:
        sql = 'select * from timetable where loc_start=? and loc_des=? order by time_start'#입력받은 출발 도착지 출력 
        start = start.upper()
        end = end.upper()
        i=1
        cur.execute(sql, (start,end))
        item_list= [(),] ## 1부터 출력 되도록
        print('''---------------------------------------------------------------------------------------------------''')
        for item in cur.fetchall():
            print(i,end=' ')
            print(f'''날짜: {item[0]}  출발지: {item[1]}  도착지: {item[2]}  출발 시간: {item[3]}  도착 시간: {item[4]} 비행기번호: {item[5]}''')
            i=i+1
            item_list.append(item)
        print('''---------------------------------------------------------------------------------------------------''')
        i= int(input('원하는 시간을 번호로 입력해 주세요 :'))
        # print(item_list[i])
        
        conn.close()
        return item_list[i]

    except Exception as e:
        conn.close()
        print(e)
        return ""