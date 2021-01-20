import radioscraper.spiders.baseSpiders.baseSpider as base

class networkWDRSpider(base.baseSpider):
    network = 'wdr'
    def get_loop(self, response):
        return response.css('tr.data:not(:first-child)')
    
    def get_date(self, response, item, counter):
        datetime = item.css('th::text').extract()
        return self.gerdatetoiso(datetime[0].replace(",",""))
    
    def get_time(self, response, item, counter):
        datetime = item.css('th::text').extract()
        return datetime[1].split(" ")[0].replace(".", ":")

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(3)::text').extract_first()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(2)::text').extract_first()