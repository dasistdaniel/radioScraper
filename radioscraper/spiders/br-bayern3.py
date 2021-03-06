import radioscraper.spiders.baseSpiders.baseBR as network

class stationSpider(network.networkBRSpider):
    name = "br-bayern3"
    station = "Bayern 3"
    start_urls = ['https://www.bayern3.radio/playlist/']

    def get_loop(self, response):
        return response.css('div.plElement')

    def get_date(self, response, item, counter):
        return self.gerdatetoiso(response.css('h2::text').extract_first().strip()[-10:])

    def get_time(self, response, item, counter):
        return item.css('.plTime::text').extract_first()

    def get_artist(self, response, item, counter):
        return item.css('div.plSong > span::text').extract_first()

    def get_title(self, response, item, counter):
        return item.css('div.plSong > strong::text').extract_first()