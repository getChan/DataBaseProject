import pymysql
from Genie_Chart_Crawling import getData

#GenieTodB()
def GenieTodB(ymd): 
    # MySQL Connection 연결
    conn = pymysql.connect('보안')    
    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()    
    # SQL문 실행
    for pn in range(1, 3):    
        for i in getData(ymd, str(pn)):
            #print(i)
            #print(ymd+hour, i[0], i[1], i[2], i[3])
            sql = "INSERT INTO zuzak.genie VALUES (%s, %s, %s, %s)"
            val = (ymd, i[0], i[1], i[2])
            curs.execute(sql, val)
            # 데이타 Fetch
            curs.fetchone()
            pass
        pass
    
    #커밋
    conn.commit()
    print(ymd+'complete')
    curs.close()
    # Connection 닫기
    conn.close()
    return


# Connection 닫기
