import func_jh as jh




check = 0
loc_list = []
print(''' 환영합니다!! ''')
while True:
    
    menu = input("""
    ---------------------------------------
              항공권 예매 프로그램
    ---------------------------------------
    1. 로그인 2. 회원가입 3.종료 >>>
    """)

    if menu == '1':
        check = jh.login_user()
        # if check == 1 :
            # user.dept_loc()
            # list = jh.loc_start()
            # start = input(f'''출발지({list[0]},{list[1]},{list[2]},{list[3]})를 입력하세요>>>''')
            # loc_dept =jh.loc_depart()
            # depart = input(f'''도착지{loc_dept[0]},{loc_dept[1]}를 선택해주세요>>>''')
            # print(start)
            # print(depart)


    elif menu =='2':
        try:
            jh.join_user()
            print('회원가입 완료')
        except Exception as e:
            print(e)

    elif menu in('3','Q','q'):
        print('프로그램 종료')
        break

    else:
        print('다시 입력해주세요.')