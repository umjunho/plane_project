import func
import fun2
import func3

check = 0
loc_list = []
login = ""  # 유저가 로그인하면 해당 값을 가지고 있음
print(''' 환영합니다!! ''')
while True:
    if login == "": #로그인 상태가 아닐경우
        menu = input("""
---------------------------------------------------------------------------------------------------
                            항공권 예매 프로그램
---------------------------------------------------------------------------------------------------
                1. 로그인 2. 회원가입 3.관리자 4.종료 >>>""")

        if menu == '1': #로그인
            login = func.login_user()

        elif menu =='2': #회원가입
            try:
                login = func.join_user()
                print('회원가입 완료')
            except Exception as e:
                print(e)

        elif menu == '3': #관리자
            login = func3.login_manager()
            while login != "":
                login = func3.manager_window()
            
        elif menu in('4','Q','q'):
            print('프로그램 종료')
            break
        
        else:
            print('다시 입력해주세요.')
    else: #로그인 완료된 상태
        menu = input("""
--------------------------------------------------------------------------------
                            항공권 예매 프로그램
--------------------------------------------------------------------------------
1.예매 2.티켓확인 3.회원정보확인 4.회원정보수정 5.로그아웃 6.종료 >>>""")
        if menu == '1': # 예매
            while True:
                check = 0
                choice = input('1.좌석확인 2.예약 확인 3.뒤로가기 >>>')
                if choice == '1':
                    print('''---------------------------------------------------------------------------------------------------''')
                    count = input('1.왕복 티켓 2.편도 티켓 >>>')  # 왕복/편도 선택
                    if count == '1': #왕복일떄
                        seat_price=0 #해당 시트값
                        sum_price = 0 #총합
                        res = func.ticketing() #출발지,도착지,시간표 출력
                        if res =="": #잘못입력된 값이 들어올때
                            break
                        print('''---------------------------------------------------------------------------------------------------''')
                        fun2.select_seat(res) #시트출력
                        while check == 0:
                            seat = input('선택하고 싶은 좌석을 선택하세요.').upper()
                            seat_price=fun2.seat_price(seat)
                            print('seat가격 : ' ,end='')
                            print(seat_price,'원')
                            print('''---------------------------------------------------------------------------------------------------''')
                            menu=input('1.결제  2.뒤로가기 >>>')
                            if menu == '1': #결제
                                check = fun2.insert_seat(login,res,seat) #쿼리문이 잘되야 check = 1
                                if check == 1 :
                                    print('결제완료')
                                    sum_price += seat_price #총합에 더하기
                                    break
                            elif menu == '2': #결제안함
                                check =2
                        if check == 2:
                            break                        
                        
                        res = func.ticketing2(res[2], res[1])    # 왕복 -2 
                        if res =="": #잘못입력된 값이 들어올때
                            break
                        fun2.select_seat(res) #시트출력
                        check = 0
                        print('''---------------------------------------------------------------------------------------------------''')
                        while check != 1:
                            seat = input('선택하고 싶은 좌석을 선택하세요 >>>').upper()
                            seat_price=fun2.seat_price(seat)
                            print('seat가격 : ' ,end='')
                            print(seat_price,'원')
                            print('''---------------------------------------------------------------------------------------------------''')
                            menu=input('1.결제  2.뒤로가기 >>>')
                            if menu == '1':
                                check = fun2.insert_seat(login,res,seat) #쿼리문이 잘되야 check = 1
                                if check == 1 :
                                    print('결제완료')
                                    sum_price += seat_price #총합에 더하기
                                    print(f'총합은 {sum_price}원 입니다.')
                                    break
                            elif menu == '2':
                                check =2
                        if check == 2:
                            break   
                        
                    elif count == '2':   # 편도 <- 왕복이랑 비슷
                        seat_price=0
                        res = func.ticketing()
                        if res =="":
                            break
                        fun2.select_seat(res)
                        while check == 0:
                            seat = input('선택하고 싶은 좌석을 선택하세요 >>>').upper()
                            seat_price=fun2.seat_price(seat)
                            print('seat가격 : ' ,end='')
                            print(seat_price,'원')
                            menu=input('1.결제  2.뒤로가기 >>>')
                            if menu == '1':
                                check = fun2.insert_seat(login,res,seat)
                                if check == 1 :
                                    print('결제완료')
                                    break
                            elif choice == '2':
                                break

                elif choice == '2':
                    func.check_ticket(login)   # 티켓 확인 함수 호출
                elif choice =='3':
                    break
                else:
                    print('다시 입력해주세요.')
    
        elif menu == '2':   # 예약한 티켓 확인/삭제
            func.check_ticket(login)
            choice = input('1.뒤로가기 2.예매 취소 >>>')
            if choice=='2':
                fun2.ticket_del(login)
            elif choice =='1':
                pass
        elif menu == '3':   #회원 정보 확인
            func.check_info(login)

        elif menu == '4':   # 회원 정보 수정
            func.update_userinfo(login)

        elif menu == '5':  # 로그아웃
            login = ""
            print('안전하게 로그아웃 되었습니다.')

        elif menu in('6','Q','q'):
            print('프로그램 종료')
            break

        else:
            print('         다시 입력해주세요.')
