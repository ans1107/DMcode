#1. Create Project

#2. Item Class
from scrapy.item import Item, Field

class NewsCommentItem(Item):
	nickname = Field()
	cmt = Field()
	date = Field()

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from NewsComment.items import NewsCommentItem

class MySpider(BaseSpider):
	name = "NewsComment"
	allowed_domains = ["comment.news.naver.com/"]
	start_urls = ["http://comment.news.naver.com/comment/all.nhn?serviceId=news&gno=news421,0001207435&sort=newest&page=2"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		names = hxs.select("//div[@class='author']")
		for names in names:
			nickname = names.select("span/text()").extract()
			link = titles.select("a/@href").extract()
			print title, link