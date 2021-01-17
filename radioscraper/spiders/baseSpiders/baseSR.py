import radioscraper.spiders.baseSpiders.baseSpider as base
import datetime

class srSpider(base.baseSpider):
    network = 'sr'
    def get_loop(self, response):
        return response.css('.musicResearch__Item')
    
    def get_date(self, response, item, counter):
        return datetime.datetime.now().strftime('%Y-%m-%d')
    
    def get_time(self, response, item, counter):
        return response.css('.musicResearch__Item__Time::text').extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('.musicResearch__Item__Content__Artist::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('.musicResearch__Item__Content__Title::text').extract_first().strip().lower()