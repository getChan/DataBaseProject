from dbQuery import dbQuery, dfFilter, dfPlot

# 다른 노래 차트진입일
def chartInDays(title, artist, dbname):
    # 쿼리문 입력
    query = " SELECT * FROM zuzak."+dbname+" where title != \""+title+"\" and artist = \""+artist+"\" and YYMMDD<= (select YYMMDD from zuzak."+dbname+" where title = \""+title+"\" order by YYMMDD limit 1); "
    
    Chartdf = dbQuery(query)
    Chartdf = dfFilter(Chartdf)
    
    
    # 쿼리결과 없으면
    if Chartdf.empty:
        return 0
        
    # 쿼리 결과
    else :        
        return len(Chartdf)


# 랭킹 상승 평균치
def rankIncreaseMean(title, dbname):
    # 쿼리문 입력
    query = """ SELECT * FROM zuzak."""+dbname+""" where title = \""""+title+"""\" and YYMMDD<=
    (select YYMMDD from zuzak."""+dbname+""" where title = \""""+title+"""\" and cast(ranking as unsigned) <=5 order by YYMMDD limit 1); """
    
    Chartdf = dbQuery(query)
    Chartdf = dfFilter(Chartdf)
    
    # 쿼리결과 없으면
    if Chartdf.empty:
        return 0
        
    # 쿼리 결과
    elif len(Chartdf) == 1 :
        sum = 100-Chartdf['ranking'].iloc[0]
        return sum
    
    else:
        sum = 0
        a = len(Chartdf)
        
        for i in range(1, a):
            num = (Chartdf['ranking'].iloc[i-1]) - (Chartdf['ranking'].iloc[i])
            sum = sum + num
        
        return sum/(a-1)
    

# 5위 진입 전까지 일수
def rankInDays(title, dbname):
    # 쿼리문 입력
    query = """ SELECT * FROM zuzak."""+dbname+""" where title = \""""+title+"""\" and YYMMDD<=(SELECT YYMMDD FROM zuzak."""+dbname+""" where title = \""""+title+"""\" and cast(ranking as unsigned) <=5  order by YYMMDD limit 1); """
    Chartdf = dbQuery(query)
    Chartdf = dfFilter(Chartdf)
    
    # 쿼리결과 없으면
    if Chartdf.empty:
        return 0
        
    # 쿼리 결과
    else :
        return len(Chartdf)