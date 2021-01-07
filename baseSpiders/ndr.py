import baseSpiders.baseSpider

class ndrSpider(baseSpiders.baseSpider.baseSpider):
    def get_loop(self, response):
        return response.css('li.program')
    
    def get_date(self, response, item, counter):
        return self.gerdatetoiso(response.css('option:checked::text').extract_first())
    
    def get_time(self, response, item, counter):
        return item.css('div.timeandplay > strong::text').extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('span.artist::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('span.title::text').extract_first().strip().lower()