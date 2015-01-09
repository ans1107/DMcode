from bs4 import BeautifulSoup
import urllib2

# 1. Get html page
url = 'http://m.news.naver.com/read.nhn?oid=056&aid=0010114544&sid1=101&mode=LSD'

# 1.1 Simple code
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


# 2. Extract informations which we want to Get

# 2.1 Extracting division
cmt_list = soup.find_all('div',{'class': 'comment_area _comment_area comment_area_over'})
#cmt = cmt_list.find('p').text.encode('utf-8')
print cmt_list

