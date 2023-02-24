
import sqlite3,os,re
import pandas as pd
path = os.path.dirname(__file__)

# 관리자 시간표, 비행기, 시트

def login_manager():
    conn = sqlite3.connect(path+'/table.db')
    id_pw = pd.read_sql_query("select manager_id, manager_pw from manager", conn).values #dataframe값을 리스트로 인덱스 없이 추출하는 코드
    check =0
    login = ""

    id_ox = input("ID를 입력해주세요 >>")
    for i in range(len(id_pw)):
        if id_ox == id_pw[i][0]: #db에 user_id값이 있는지 확인하는 코드 / 중복제거
            pw = input(f"""
|로그인|
---------------------------
ID: {id_ox}
패스워드 >>""")
            check = 1
            if pw == id_pw[i][1]:
                print("""로그인 완료!""")
                login = id_pw[i][0]
            else:
                print("비밀번호가 올바르지않습니다.")
                
    if check == 0:
        print("일치하는 id가 존재하지 않습니다.")

    conn.close()
    return login

#관리자가 로그인하면 뜨는 화면
def manager_window():
    menu = input("""
--------------------------------------------------------------------------------
                            관리자 프로그램
--------------------------------------------------------------------------------
1. 시간표 관리 2. 비행기 관리 3.시트 관리 4.로그아웃 >>>""")
    if menu == '1':
        manager_timetable()
    elif menu =='2':
        manager_airplane()
    elif menu =='3':
        manager_seat()
    elif menu =='4':
        return ""
    else:
        print('잘못 입력하셨습니다.')

#관리자가 시트를 추가하는 화면
def manager_seat():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    menu = input("""
1. 시트 추가 2. 시트 삭제 3.뒤로가기 >>>""")
    if menu == '1': #시트 추가하기 insert문
        try:
            sql =('''
insert into seat values(?,?,?)
''')    
            seat_code = input('시트코드를 입력하세요 >>>')
            seat_price = input('시트가격을 입력하세요 >>>')
            air_name = input('비행기 이름을 입력하세요 >>>')
            cur.execute(sql, (seat_code,seat_price,air_name))
            conn.commit()
        except:
            print('잘못 입력하셨습니다.')
    
    elif menu =='2':#시트 삭제하기 delete문 / primary가 없어 seat_code와 air_name을 이용함
        try:
            sql =('''delete from seat where seat_code = (?) and air_name = (?)''')    
            seat_code = input('삭제할 시트코드를 입력하세요 >>>')
            air_name = input('삭제할 비행기 이름을 입력하세요 >>>')
            cur.execute(sql, (seat_code,air_name))
            conn.commit()
        except Exception as e:
            print(e)
            print('잘못 입력하셨습니다.')
    elif menu =='3':
        pass
    else:
        print('잘못 입력하셨습니다..')
    conn.close()

#비행기 관리
def manager_airplane():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    menu = input("""
1. 비행기 추가 2. 비행기 삭제 3.뒤로가기 >>>""")
    if menu == '1': #비행기 추가 insert문
        try:
            sql =('''
insert into airplane values(?,?)
''')    
            air_name = input('비행기 이름을 입력하세요 >>>')
            capacity = input('수용인원을 입력하세요 >>>')
            cur.execute(sql, (air_name,capacity))
            conn.commit()
        except:
            print('잘못 입력하셨습니다.')
    
    elif menu =='2': #비행기 삭제 delete문 /  primry키인 air_name이용
        try:
            sql =('''delete from airplane where air_name = (?)''')    
            air_name = input('삭제할 비행기 이름을 입력하세요 >>>')
            cur.execute(sql, (air_name,))
            conn.commit()
        except Exception as e:
            print(e)
            print('잘못 입력하셨습니다.')
    elif menu =='3':
        pass
    else:
        print('잘못 입력하셨습니다..')
    conn.close()


#시간표 관리함수
def manager_timetable():
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    menu = input("""
1. 시간표 추가 2. 시간표 삭제 3.뒤로가기 >>>""")
    if menu == '1': #시간표 추가 insert문
        try:
            sql =('''
insert into timetable values(?,?,?,?,?,?)
''')    
            time_num = input('시간번호를 입력하세요 >>>')
            loc_start = input('출발지를 입력하세요 >>>')
            loc_des =input('도착지를 입력하세요 >>>')
            time_start = input('출발시간을 입력하세요 >>>')
            time_des = input('도착시간을 입력하세요 >>>')
            air_name = input('비행기명을 입력하세요 >>>')
            cur.execute(sql, (time_num,loc_start,loc_des,time_start,time_des,air_name))
            conn.commit()
        except:
            print('잘못 입력하셨습니다.')
     
    elif menu =='2': #시간표 삭제 delete문 / primary키인 time_num 이용
        try:
            sql =('''delete from timetable where time_num = (?)''')    
            time_num = input('삭제할 시간번호를 입력하세요 >>>')
            cur.execute(sql, (time_num,))
            conn.commit()
        except Exception as e:
            print(e)
            print('잘못 입력하셨습니다.')

    elif menu =='3':
        pass
    else:
        print('잘못 입력하셨습니다..')
    conn.close()
