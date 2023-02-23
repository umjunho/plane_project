import func
import fun2

check = 0
loc_list = []
login = ""
print(''' 환영합니다!! ''')
while True:
    
    menu = input("""
--------------------------------------------------------------------------------
                              항공권 예매 프로그램
--------------------------------------------------------------------------------
1. 로그인 2. 회원가입 3.예매 4.티켓확인 5.회원정보확인 
6.회원정보수정 7.로그아웃 8.종료 >>>""")

    if menu == '1':
        if login == "":
            login = func.login_user()
        else:
            print(f'{login}님 이미 로그인이 되어있습니다.')

    elif menu =='2':
        if login != "":
            print(f'{login}님 이미 로그인이 되어있습니다.')
        else:
            try:
                login = func.join_user()
                print('회원가입 완료')
            except Exception as e:
                print(e)

    elif menu == '3':
        if login == "":
            print('로그인 상태가 아닙니다.')
        else:
            # 왕복이냐 아니냐
            res = func.ticketing()
            print(res)
            seat = fun2.select_seat(res)
            print(seat)
            # seat = fun2.select_seat(res)#좌석
            fun2.insert_seat(login,res, seat) #예매값올리기 + 표내용 찍어주기

    elif menu == '4':
        if login == "":
            print('로그인 상태가 아닙니다.')
        else:
            func.check_ticket(login)

    elif menu == '5':
        if login == "":
            print('로그인 상태가 아닙니다.')
        else:
            func.check_info(login)

    elif menu == '6':
        if login == "":
            print('로그인 상태가 아닙니다.')
        else:
            func.update_userinfo(login)

    elif menu == '7':
        if login != "":
            login = ""
            print('안전하게 로그아웃 되었습니다.')
        else:
            print('로그인 상태가 아닙니다.')

    elif menu in('8','Q','q'):
        print('프로그램 종료')
        break

    else:
        print('다시 입력해주세요.')
