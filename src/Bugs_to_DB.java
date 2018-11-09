package DBP;

import java.util.Scanner;
import java.io.IOException;
import java.sql.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
 
public class Bugs_title_Search {
 
     
    public static void main(String[] args) {
        // Jsoup를 이용해서 벅스 노래차트 크롤링
    	
    	
        Scanner sc = new Scanner(System.in);
        
        System.out.print("제목 검색 : ");
        String Song_name=sc.next();
        System.out.print("시작 YYMMDD 입력 : ");
        int chardate=sc.nextInt();
        System.out.print("시작 HH 입력 : ");
        int hour = sc.nextInt();
        System.out.print("종룔 YYMMDD 입력 : ");
        int from_chardate = sc.nextInt();

        int i=1;
        int k=1;
        int cnt=0;
        int key = 0;
        String ranking[] = new String[101];
        String insert_ranking[] = new String[101];
        String insert_title[] = new String[101];
        String insert_artist[] = new String[101];
        String insert_date;
        
       
        for(;chardate<=from_chardate;chardate++) {
         insert_date = ""+chardate+""+hour;
         String url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate="+chardate+"&charthour="+hour;
         Document doc = null;
          
         try {
             doc = Jsoup.connect(url).get();
         } catch (IOException e) {
             e.printStackTrace();
         }
          
         // 주요 뉴스로 나오는 태그를 찾아서 가져오도록 한다.
         Elements element = doc.select("div.innerContainer"); // innerContainer 자료 가져오기
         
         for(Element el : element.select("div.ranking")) { // 1~100위 노래 차트 저장
             	ranking[i] = el.text();
             	i++;
         }
         for(int j=1;j<=100;j++)
         {
         	if(j <10 ) {
         		insert_ranking[j] = ranking[j].substring(0,1);
         	}
         	else if(j>=10 && j<=99){
         		insert_ranking[j] = ranking[j].substring(0,2);
         	}
         	else {
         		insert_ranking[j] = ranking[j].substring(0,3);
         	}
         }
         i=1;          
         
         for(Element el : element.select("p.title")) { // 1~100위 노래제목 저장
             insert_title[k] = el.text();
         	k++;
         }
         k=1;
         
         for(Element el : element.select("p.artist")) { // 1~100위 노래가수 저장
         	insert_artist[k] = el.text();
         	k++;
         }
         k=1;
             
         for(Element el : element.select("p.title")) {    // for문 이용하여 1~100위 가수 출력
        	 cnt++;
        	 if(Song_name.equals(el.text())) {
        		 key=cnt;
                 System.out.println(insert_date+" 순위 "+insert_ranking[key]+" 제목 "+insert_title[key]+" 가수 "+insert_artist[key]);
        		 break;
        	 }
            }
         key=0;
         cnt=0;
         

            
         
/*         // DB연결
        Connection conn = null;
        PreparedStatement pstmt = null;
        Statement stmt = null;
        ResultSet rs = null;
     
        try {
            Class.forName("com.mysql.jdbc.Driver");
            System.out.println("Dvrver is Loadded");
            String Durl = "jdbc:mysql://zuzak.cvqcrkck1aqg.us-east-1.rds.amazonaws.com?useUnicode=true&characterEncoding=euc_kr";
            String user = "getChan";
            String pass = "cksdl951!!";
            conn = DriverManager.getConnection(Durl, user, pass);
            stmt = conn.createStatement();
            
            String sql = "insert into zuzak.bugs values(?,?,?,?)"; //mysql에 저장하기 위한 쿼리문
            pstmt = conn.prepareStatement(sql);
            
            for(int j=1;j<=100;j++)
            {
            pstmt.setString(1, insert_date);
            pstmt.setString(2, insert_ranking[key]);
            pstmt.setString(3, insert_title[key]);
            pstmt.setString(4, insert_artist[key]);
            
            pstmt.executeUpdate();
            }
            System.out.println("레코드 추가 완료");

        } catch (Exception e) {
            System.out.println(e);
        }finally {
            try {
                if(rs != null)rs.close();
                if(stmt !=null)stmt.close();
                if(conn!=null)conn.close();
            }catch(SQLException e) {}
        }*/
       }
    }
}
