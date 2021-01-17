import radioscraper.spiders.baseSpiders.baseSpider as base

class rbbSpider(base.baseSpider):
    network = 'rbb'
    def get_loop(self, response):
        return response.css('tr:not(:first-child)')
    
    def get_date(self, response, item, counter):
        return self.gerdatetoiso(item.css('td:nth-child(1)::text').extract_first())
    
    def get_time(self, response, item, counter):
        return item.css('td:nth-child(2)::text').extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(3)::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(4)::text').extract_first().strip().lower()