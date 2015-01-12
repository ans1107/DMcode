from bs4 import BeautifulSoup
import urllib2

# 1. Get News URL from Date


# 2. Get Reply Page from News URL
#  gno=news[기사 url oid number],[기사 url aid number]
#oid = "421" # revise!
#aid = "0001207435" # revise!
#gno = "gno=news"+oid+aid
#url = "http://comment.news.naver.com/comment/all.nhn?serviceId=news&"+gno+"&sort=newest&page=2"
url = 'http://comment.news.naver.com/comment/all.nhn?serviceId=news&gno=news421,0001207435&sort=newest&page=2'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

author = soup.find_all('div', {'class': 'author'})
nickname = author[0].find('span').text



