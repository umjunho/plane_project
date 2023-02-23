import sqlite3
import os


path = os.path.dirname(__file__)

list = []

def select_seat(res):
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    res1 =res
    name = res1[5]
    print(name)
    sql = "select * from seat where air_name = ? "
    cur.execute(sql,(name,))
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

    for item in list:
        if 'A' in item:
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

    alpha = ['A', 'B','C','D','E','F']
    print('- '*63)
    # for i in range(1,len(list1)+1):
    #     print(i,end=' ')
    # print()
    # print(seatlist)
    for idx in range(0,6):
        # print(alpha[idx],end=' ')
        for i in range(len(list1)):
            seatlist[idx][i]='□'
            # print('□', sep =' ',end=' ')
            # print(seatlist[idx][i], end=' ')
        # print()
    
    seatlist[1][2]='■'

    import pandas as pd

    df  = pd.DataFrame({
        "A":seatlist[0],
        "B":seatlist[1],
        "C":seatlist[2],
        " ":"",
        "D":seatlist[3],
        "E":seatlist[4],
        "F":seatlist[5]
    })
    df.index = range(1,34)
    df=df.transpose()
    # print(type(df))
    print(df)
    seat_num =input('선택하고 싶은 좌석을 선택하세요 >>>').upper()
    
    return seat_num

# list_seat()


def list_seat():
    select_seat()

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

    for item in list:
        if 'A' in item:
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

    alpha = ['A', 'B','C','D','E','F']
    print('- '*63)
    # for i in range(1,len(list1)+1):
    #     print(i,end=' ')
    # print()
    # print(seatlist)
    for idx in range(0,6):
        # print(alpha[idx],end=' ')
        for i in range(len(list1)):
            seatlist[idx][i]='□'
            # print('□', sep =' ',end=' ')
            # print(seatlist[idx][i], end=' ')
        # print()
    
    seatlist[1][2]='■'

    import pandas as pd

    df  = pd.DataFrame({
        "A":seatlist[0],
        "B":seatlist[1],
        "C":seatlist[2],
        " ":"",
        "D":seatlist[3],
        "E":seatlist[4],
        "F":seatlist[5]
    })
    df.index = range(1,34)
    df=df.transpose()
    # print(type(df))
    print(df)

  
# list_seat()

def insert_seat(login,res,seat):
    conn = sqlite3.connect(path+'/table.db')
    cur = conn.cursor()
    str = "111"

    sql = 'insert into reservation values(?,?,?,?,?)'
    cur.execute(sql,(str,login,seat,res[0],res[5]))
    conn.commit()
    conn.close()