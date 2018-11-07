import pymysql
from Genie_Chart_Crawling import getData

# MySQL Connection 연결
conn = pymysql.connect(host='zuzak.cvqcrkck1aqg.us-east-1.rds.amazonaws.com', user='getChan', password='cksdl951!!',
                       db='zuzak', charset='euckr')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
for i in getData('20181010', '13', '1'):
    sql = "INSERT INTO zuzak.genie VALUES (%s, %s, %s, %s)"
    val = ('18101013', i[0], i[1], i[2])
    curs.execute(sql, val)
    conn.commit()
 
# 데이타 Fetch
#rows = curs.fetchall()
#print(rows)     # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
 

# Connection 닫기
conn.close()