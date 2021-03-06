import radioscraper.spiders.baseSpiders.baseSpider as base

class networkBRSpider(base.baseSpider):
    network = 'br'
    def get_loop(self, response):
        return response.css('dd.audio')
    
    def get_date(self, response, item, counter):
        return self.gerdatetoiso(response.css('li.playlist_navi_head::text').extract_first().strip()[-10:])
    
    def get_time(self, response, item, counter):
        css = f"dt.time:nth-child({1 + counter * 2})::text"
        return response.css(css).extract_first()

    def get_artist(self, response, item, counter):
        return item.css('ul > li > span:nth-child(1)::text').extract_first()

    def get_title(self, response, item, counter):
        return item.css('ul > li > span:nth-child(2)::text').extract_first()