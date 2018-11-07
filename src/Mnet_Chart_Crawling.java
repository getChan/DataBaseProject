import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.util.Scanner;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Locale;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class date {

	public static String doDateAdd(String dates) throws ParseException { // 날짜 계산
		Calendar cal = new GregorianCalendar(Locale.KOREA); // cal 객체생성
		SimpleDateFormat fm = new SimpleDateFormat("yyyyMMddHH");// Dateform 생성

		Date date = fm.parse(dates);// 입력받은 문자열 date를 Date형식으료 변환
		cal.setTime(date);
		cal.add(Calendar.DAY_OF_YEAR, 1); // 하루를 더한다.
		String strDate = fm.format(cal.getTime());
		return strDate;
	}

	public static void main(String[] args) throws ParseException {
		// Jsoup를 이용해서 엠넷차트
		Scanner sc = new Scanner(System.in);
		System.out.println("노래 제목 검색");
		String Song_name = sc.nextLine();
		System.out.println("음원 탐색 기간 설정  (언제부터? ex) yyyyMMDDHH)");
		String to_Date = sc.next();
		System.out.println("음원 탐색 기간 설정 (언제까지? ex) yyyyMMDDHH");
		String from_Date = sc.next();
		String Artist ="";
		String Title ="";
		do {
			String url = "http://www.mnet.com/chart/TOP100/" + to_Date;
			String url2 = "http://www.mnet.com/chart/TOP100/" + to_Date +"?pNum=2";
			Document doc = null;
			Document doc2 = null;
			int cnt = 1; // 음원 차트 순위 카운팅

			try { // Jsoup
				doc = Jsoup.connect(url).get();
				doc2 = Jsoup.connect(url2).get();
			} catch (IOException e) {
				e.printStackTrace();
			}
			boolean is_song = false; // 해당 노래가 있는지 체크

			// 주요 차트를 나오는 태그를 찾아서 가져오도록 한다.
			Elements element = doc.select("div.MMLTable");
			Elements element2 = doc2.select("div.MMLTable");

			for (Element el : element.select("div.MMLITitle_Box.info")) {
				Title =el.select("a.MMLI_Song").text();
				Artist = el.select("a.MMLIInfo_Artist").text();
				if (Song_name.contains(Title)) {
					System.out.println("날짜:" + to_Date + " 제목:" + Title + " 가수 :"+ Artist +" 순위:" + cnt + "위");
					is_song = true;
					break;
				}
				cnt++;
			}
			if (!is_song) {
				for (Element el : element2.select("div.MMLITitle_Box.info")) {
					Title =el.select("a.MMLI_Song").text();
					Artist = el.select("a.MMLIInfo_Artist").text();
					if (Song_name.contains(Title)) {
						System.out.println("날짜:" + to_Date + " 제목:" + Title + " 가수 :"+ Artist +" 순위:" + cnt + "위");
						is_song = true;
						break;
					}
					cnt++;

				}
				if(!is_song) {
					System.out.println("날짜:" + to_Date + " 제목: " + Song_name + " 해당 노래가 차트에 없습니다.");
				}
			}
					

			to_Date = doDateAdd(to_Date);

		} while (!(to_Date.equals(from_Date)));
		sc.close();
	}
}
