import sqlite3
import os


path = os.path.dirname(__file__)

# res : 유저가 선택한 출발지,도착지에 해당하는 비행기 좌석 데이터를 받아오는 함수
def select_seat(res):
    list = []
    seatcheck_list = []
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    res1 = res
    name = res1[5]
    # print(name)
    sql = "select * from seat where air_name = ? "
    cur.execute(sql, (name,))
    for item in cur.fetchall():
        list.append(item[0])
    # print(list)
    conn.close()

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

# 좌석 번호가 ex) A1,B1,C1 형식으로 되어있어 해당값을 각 리스트에 담아서 관리
    for item in list:
        if 'A' in item: #A~F까지의 좌석코드
            # print(item)
            list1.append(item)
        elif 'B' in item:
            list2.append(item)
        elif 'C' in item:
            list3.append(item)
        elif 'D' in item:
            list4.append(item)
        elif 'E' in item:
            list5.append(item)
        elif 'F' in item:
            list6.append(item)

    seatlist = []

    seatlist.append(list1)
    seatlist.append(list2)
    seatlist.append(list3)
    seatlist.append(list4)
    seatlist.append(list5)
    seatlist.append(list6)

    for idx in range(len(seatlist)):
        seatcheck_list.append(seatlist[idx])
    # print('확인',seatcheck_list, res)

    # 해당 비행기에 좌석이 예매 되어있는지 확인하는 함수 호출 
    check_seat(seatcheck_list, res)

    # alpha = ['A', 'B','C','D','E','F']
    print('- '*63)

    # for i in range(1,len(list1)+1):
    #     print(i,end=' ')
    # print()
    # print(seatlist)
    # for idx in range(0,6):
    #     # print(alpha[idx],end=' ')
    #     for i in range(len(list1)):
    #         seatlist[idx][i]='□'
    #         # print('□', sep =' ',end=' ')
    #         # print(seatlist[idx][i], end=' ')
    #     # print()


# 비행기에 예약 되어있는 좌석을 메인 화면에 나타내주는 함수
def check_seat(seatcheck_list, res):
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    sql = "select seat_code from reservation where time_num=? and air_name = ? "
    # print(res)
    res1 = res[5]
    # print('res1:'+res1)
    cur.execute(sql, (res[0], res[5],))
    checkOn_seat = []
    for item in cur.fetchall():
        checkOn_seat.append(item[0])
        # print(item)

    # print(checkOn_seat)

    # 예약 되어있는 좌석은 ■, 빈 좌석 표시는 □ 표현
    for i in range(len(seatcheck_list)):
        for j in range(0, 33):
            if seatcheck_list[i][j] in (checkOn_seat):
                seatcheck_list[i][j] = '■'
            else:
                seatcheck_list[i][j] = '□'
    # print(seatcheck_list)

# 좌석 배치를 데이터프레임 형식으로 나타내줌

    import pandas as pd

    df = pd.DataFrame({
        "A": seatcheck_list[0],
        "B": seatcheck_list[1],
        "C": seatcheck_list[2],
        " ": "",
        "D": seatcheck_list[3],
        "E": seatcheck_list[4],
        "F": seatcheck_list[5]
    })
    df.index = range(1, 34)
    df = df.transpose()
    # print(type(df))
    print(df)


# 예약테이블에 정보 저장 (예약번호,아이디,좌석번호,시간테이블번호,비행기명)

def insert_seat(login, res, seat):
    check = 0
    # print(res)
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    res_num = str(f'''{res[5]}_{seat}_{res[0]}'''.strip())
    try:
        sql = 'insert into reservation values(?,?,?,?,?)'
        cur.execute(sql, (res_num, login, seat, res[0], res[5]))
        conn.commit()
        check = 1
    except Exception as e:
        print('다시 선택해주세요.')
    conn.close()

    return check


# 해당 좌석에 대한 가격을 나타내주는 함수 
def seat_price(seat):
    seat_price = 0
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    sql = 'select seat_price from seat where seat_code = ?'
    cur.execute(sql, (seat,))
    seat_price = cur.fetchone()
    return seat_price[0]



def ticket_del(login):## 티켓 삭제 
    conn = sqlite3.connect(path + '/table.db')
    cur = conn.cursor()
    sql_1= 'select res_num from reservation where user_id=?' ##로그인 id 값으로
    sql= 'delete from reservation where res_num=?'##    예매된 티켓 삭제
 
    cur.execute(sql_1,(login,))
    res_list= []
    for item in cur.fetchall():

        res_list.append(item[0])
    # print(res_list) ## 찾는 아이디의  res_num 값

    try:
        print('''---------------------------------------------------------------------------------------------------''')
        del_res=int(input('삭제할 티켓을 고르세요 >>>'))
        del_res -=1
        cur.execute(sql,(res_list[del_res],))
    except:
        print("잘못 입력하셨습니다.")
    conn.commit()
    conn.close()