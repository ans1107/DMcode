import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Navernewcmt {
    public static void main(String[] args) {
        String url;
        //url = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0007361037&date=20150118&type=1&rankingSeq=1&rankingSectionId=101";
        url = "http://comment.news.naver.com/comment/all.nhn?serviceId=news&gno=news421,0001207435&sort=newest&page=2";
        // Q. �� comment.��¼���� crawling�� �Ǵµ� ���� ������翡����crawling�� �ȵǴ°���
        
        System.setProperty("webdriver.chrome.driver",
                "C:/Program Files/chromedriver_win32/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        driver.get(url);

        for (int cnt = 1; cnt <= 20; cnt++) { // ��� ����� �ҷ����� ������ �������� ������ �ʴ� �п� ���� �ذ�, �׸��� 222����� �κ��� �ҷ��;� �Ѵ�. 
            WebElement htmlcontent = driver
                    .findElement(By
                            .xpath(".//*[@id='sc_comment_box']/div[3]/div[5]/ul/li["+cnt+"]/div[1]"));
            String comment = htmlcontent.getText();
            System.out.println(comment);
        }
    }
}
