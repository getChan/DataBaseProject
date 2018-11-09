import pymysql
from Genie_Chart_Crawling import getData

# MySQL Connection 연결
conn = pymysql.connect(host='zuzak.cvqcrkck1aqg.us-east-1.rds.amazonaws.com', user='getChan', password='cksdl951!!',
                       db='zuzak', charset='euckr')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
ymd = '180810'
hh = '13'
# SQL문 실행
for pn in range(1, 3):    
    for i in getData(ymd, hh, str(pn)):
        print(i)
        sql = "INSERT INTO zuzak.genie VALUES (%s, %s, %s, %s, %s)"
        val = (ymd+hh, i[0], i[1], i[2], i[3])
        curs.execute(sql, val)
        # 데이타 Fetch
        rows = curs.fetchone()
        pass
    pass
        
#커밋
conn.commit()
 


#cursor 닫기 
curs.close()
# Connection 닫기
conn.close()