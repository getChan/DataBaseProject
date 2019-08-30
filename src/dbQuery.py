import pymysql
import pandas as pd
from matplotlib import pyplot as plt

# 쿼리를 입력하면 db에 있는 데이터를 pandas DataFrame형태로 반환
def dbQuery(query):
    
    conn = pymysql.connect('보안')
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
