import radioscraper.spiders.baseSpiders.baseSpider as base

class networkHRSpider(base.baseSpider):
    network = 'hr'
    def get_loop(self, response):
        return response.css('li.c-epgBroadcast__item')
    
    def get_date(self, response, item, counter):
        try: return item.css('.c-epgBroadcast__startTime > time::attr(datetime)').extract_first()[:10]
        except: return None

    def get_time(self, response, item, counter):
        try: return item.css('.c-epgBroadcast__startTime > time::text').extract_first()
        except: return None

    def get_artist(self, response, item, counter):
        try: return item.css('div:nth-child(2) > span:nth-child(2) > span:nth-child(1) > span:nth-child(1)::text').extract_first()
        except: return None

    def get_title(self, response, item, counter):
        try: return item.css('div:nth-child(2) > span:nth-child(1)::text').extract_first()
        except: return None