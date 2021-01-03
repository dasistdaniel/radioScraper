import baseSpiders.baseSpider

class wdrSpider(baseSpiders.baseSpider.baseSpider):
    def get_loop(self, response):
        return response.css('tr.data:not(:first-child)')
    
    def get_date(self, item):
        datetime = item.css('th::text').extract()
        return  datetime[0].replace(",","")
    
    def get_time(self, item):
        datetime = item.css('th::text').extract()
        return datetime[1].split(" ")[0].replace(".", ":") + ":00"

    def get_artist(self, item):
        return item.css('td:nth-child(3)::text').extract_first().strip().lower()

    def get_title(self, item):
        return item.css('td:nth-child(2)::text').extract_first().strip().lower()
