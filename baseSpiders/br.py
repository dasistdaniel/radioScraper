import baseSpiders.baseSpider

class brSpider(baseSpiders.baseSpider.baseSpider):
    def get_loop(self, response):
        return response.css('dd.audio')
    
    def get_date(self, response, item, counter):
        return response.css('li.playlist_navi_head::text').extract_first().strip()[-10:]
    
    def get_time(self, response, item, counter):
        print (counter)
        #return response.css("dt.time:nth-child(" + counter + ")").extract()
        return "yaaa"

    def get_artist(self, response, item, counter):
        return item.css('ul > li > span:nth-child(1)::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('ul > li > span:nth-child(2)::text').extract_first().strip().lower()

