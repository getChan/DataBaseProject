import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
 
public class JsoupTest {
 
    /*
     *  Document 클래스 : 연결해서 얻어온 HTML 전체 문서
     *  Element 클래스  : Documnet의 HTML 요소
     *  Elements 클래스 : Element가 모인 자료형
     */
     
    public static void main(String[] args) {
        // Jsoup를 이용해서 엠넷차트
        String url = "http://www.mnet.com/chart/TOP100/2018011013";
        Document doc = null;
         
        try {
            doc = Jsoup.connect(url).get();
        } catch (IOException e) {
            e.printStackTrace();
        }
         
        // 주요 차트를 나오는 태그를 찾아서 가져오도록 한다.
        Elements element =doc.select("div.MMLTable");

         
        // 1. 헤더 부분의 제목을 가져온다.
        String title = element.select("caption").text().substring(0, 10);

 
        System.out.println("============================================================");
        System.out.println(title);
        System.out.println("============================================================");
         
        int rank=1;
       for(Element el : element.select("div.MMLITitleSong_BOX")) {    // 하위 차트들을 for문 돌면서 출력
            System.out.println(rank+" "+el.text());
            rank++;
        }

        System.out.println("============================================================");
    }
 
}
