import baseSpiders.baseSpider

class brSpider(baseSpiders.baseSpider.baseSpider):
    def get_loop(self, response):
        return response.css('dd.audio')
    
    def get_date(self, response, item):
        return response.css('li.playlist_navi_head::text').extract_first().strip()[-10:]
    
    def get_time(self, response, item):
        #return  item.css('ul').extract()
        return ""

    def get_artist(self, response, item):
        return item.css('ul > li > span:nth-child(1)::text').extract_first().strip().lower()

    def get_title(self, response, item):
        return item.css('ul > li > span:nth-child(2)::text').extract_first().strip().lower()

