import scrapy
# (from module name) import module function

scrapy crawl NaverNews

class NewsItem(scrapy.Item): # Scraping Data definition 
	body = scrapy.Field()
	image = scrapy.Field()

class NewsSpider(scrapy.Spider): # mandatory attributes: name, start_urls, parse()
	# identifies the Spider. must be unique
	name = "NaverNews"
	allowed_domains = ["naver.com"]

	# list of Urls where the spider will begin to crawl from.
	start_urls = ["http://news.naver.com/main/hotissue/read.nhn?mid=hot&sid1=100&cid=1005833&iid=25174678&oid=001&aid=0007324786&ptype=011"]
	
	# method of the spider. parsing the response data and extracting data
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
		

	
