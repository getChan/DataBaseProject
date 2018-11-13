import pymysql
import pandas as pd
from matplotlib import pyplot as plt

# 쿼리를 입력하면 db에 있는 데이터를 pandas DataFrame형태로 반환
def dbQuery(query):
    
    conn = pymysql.connect(host='zuzak.cvqcrkck1aqg.us-east-1.rds.amazonaws.com', user='getChan', password='cksdl951!!',db='zuzak', charset='euckr')
    q = query
    try:
        with conn.cursor() as cursor:
            df = pd.read_sql(q, con=conn)
            cursor.fetchall()
    finally:
        conn.close()
        return df

# DataFrame 전처리 함수.
def dfFilter(dataFrame):
    df = dataFrame.set_index("YYMMDD")
    df.ranking =pd.to_numeric(df.ranking)

    return df

# dataFrame 시각화
def dfPlot(dataFrame):
    dataFrame.plot()
    plt.gca().invert_yaxis()
    plt.ylabel('ranking')
    plt.show()

# 메인함수
if __name__ == "__main__":
    # 쿼리문 입력
    query = "SELECT * FROM zuzak.genie where title = '이소설의끝을다시써보려해' order by YYMMDD;"

    df = dbQuery(query)
    df = dfFilter(df)

    # 쿼리 결과
    print(df)
    
    #시각화
    dfPlot(df)

    #데이터 정보 출력
    print(df.describe())

    #데이터 피어슨 상관계수
    print(df.corr(method='pearson'))