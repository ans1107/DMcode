from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist.items import CraigslistSampleItem

class MySpider(BaseSpider):
	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/search/npo/"]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//span[@class='p1']")
		items = []
		for title in titles:
			item = CraigslistSampleItem()
			item["title"] = title.select("a/text()").extract()
			item["link"] = title.select("a/@href").extract()
			items.append(item)
		return items