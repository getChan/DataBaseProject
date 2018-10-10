import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
 
public class Crowling_Music {
 
    /*
     *  Document 클래스 : 연결해서 얻어온 HTML 전체 문서
     *  Element 클래스  : Documnet의 HTML 요소
     *  Elements 클래스 : Element가 모인 자료형
     */
     
    public static void main(String[] args) {
        // Jsoup를 이용해서 벅스 노래차트 크롤링
        String url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20160830&charthour=13";
        Document doc = null;
         
        try {
            doc = Jsoup.connect(url).get();
        } catch (IOException e) {
            e.printStackTrace();
        }
         
        // 주요 뉴스로 나오는 태그를 찾아서 가져오도록 한다.
        Elements element = doc.select("div.innerContainer"); // innerContainer 자료 가져오기
        
        for(Element el : element.select("div.ranking")) {    // for문 이용하여 1~100위 노래 차트와 변동사항 출력
            System.out.println(el.text());
        }
        
        System.out.println();
        System.out.println("1위부터 100위 노래 타이틀\n");
        
        for(Element el : element.select("p.title")) {    // for문 이용하여 1~100위 노래제목 출력
            System.out.println(el.text());
        }
        
        
         
        System.out.println("============================================================");
    }
 
}
