import re ,sqlite3,os
import pandas as pd

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '\\table.db')
cur = conn.cursor()
save = pd.read_sql_query("select user_id,user_pw from user", conn)

while True:
    menu = input("""
    ---------------------------------------
              항공권 예매 프로그램
    ---------------------------------------
    1. 로그인 2. 회원가입 3.종료
    >>>
    """)
    login = 0
    if menu in ("1","로그인"):
        check =0
        count = 1
        
        id_pw = pd.read_sql_query("select user_id, user_pw from user", conn).values 
        #user 테이블의 user_id와 user_pw 의 값만 리스트로 가져오는 코드 출력 예:[['id_1', 'pw_1'], ['id_2', 'pw_2']]
    
        
        while True:
            id_ox = input("ID를 입력해주세요 >>")
            for i in range(len(id_pw)):
                if id_ox == id_pw[i][0]: #db에 user_id값이 있는지 확인하는 코드
                    pw = input(f"""
                        |로그인|
                        ---------------------------
                        ID: {id_ox}
                        패스워드 >>
                    """)
                    check = 1
                    if pw == id_pw[i][1]:
                        print("""로그인 완료!""")
                        login = 1
                    else:
                        print("비밀번호가 올바르지않습니다.")
                        


            if check == 0:
                print("일치하는 id가 존재하지 않습니다.")

            break


    elif menu in ("2","회원가입"): #id,이름, 전화번호, 주민등록, 이메일(null가능), 패스워드 
        
        while True:
            user_id = input("사용하실 ID를 입력하세요 >>")
            id_pw = pd.read_sql_query("select user_id, user_pw from user", conn).values
            check = 0
            for i in range(len(id_pw)):
                if user_id == id_pw[i][0]:
                    print("사용할 수 없는 ID입니다.")
                    check = 1
                    break
            if check == 0:
                
                user_pw = input("비밀번호를 입력하세요 >>")
                user_name = input("이름을 입력하세요 >>")
                

                while True:
                    user_tel = input("전화번호를 입력하세요 >>")
                    p = re.compile('^010[-][0-9]{4}[-][0-9]{4}')
                    if p.match(user_tel)!=None:
                        break
                    else:
                        print('010로 시작하며 -를 포함한 정확한 전화번호를 입력하세요')

                
                while True:
                    user_jumin = input("주민등록 번호를 입력하세요 >>")
                    p = re.compile('[0-9]{6}[-][0-9]{7}')
                    if p.match(user_jumin)!=None:
                        break
                    else:
                        print('-를 포함한 정확한 주민등록 번호를 입력하세요')


                while True:
                    user_email = input("email을 입력하세요 >>")
                    p = re.compile('[\S]@[a-z]{2,}[.][a-z]{2,}')
                    if p.search(user_email)!=None:
                        break
                    else:
                        print('@를 포함한 정확한 이메일을 입력하세요')

                print(user_id,user_pw,user_name,user_tel,user_jumin,user_email)
        

    elif menu in ("3","종료"):
        break







    # if check == 1:
    #     while True:
    #         menu2 = input("""
    #         ---------------------------------------
    #                       항공기 예매
    #         ---------------------------------------

    #         """)



conn.commit()
conn.close()
