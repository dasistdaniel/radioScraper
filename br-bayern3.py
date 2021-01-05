import baseSpiders.br as br

class br3Spider(br.brSpider):
    name = "bayern3"
    start_urls = ['https://www.bayern3.radio/playlist/']

    def get_loop(self, response):
        return response.css('div.plElement')
    
    def get_date(self, response, item, counter):
        return response.css('h2::text').extract_first().strip()[-10:]
    
    def get_time(self, response, item, counter):
        return item.css('.plTime::text').extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('div.plSong > span::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('div.plSong > strong::text').extract_first().strip().lower()