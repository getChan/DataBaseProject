import pymysql
from Genie_Chart_Crawling import getData

# MySQL Connection 연결
conn = pymysql.connect(host='zuzak.cvqcrkck1aqg.us-east-1.rds.amazonaws.com', user='getChan', password='cksdl951!!',
                       db='zuzak', charset='euckr')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()    
#GenieTodB()
def GenieTodB(ymd, hour): 
    
    # SQL문 실행
    for pn in range(1, 3):    
        for i in getData(ymd, hour, str(pn)):
            #print(i)
            #print(ymd+hour, i[0], i[1], i[2], i[3])
            sql = "INSERT INTO zuzak.genie VALUES (%s, %s, %s, %s, %s)"
            val = (ymd+hour, i[0], i[1], i[2], i[3])
            curs.execute(sql, val)
            # 데이타 Fetch
            curs.fetchone()
            pass
        pass
    
    #커밋
    conn.commit()
    
    return


# Connection 닫기
