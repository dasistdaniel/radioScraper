import radioscraper.spiders.baseSpiders.baseRB as network

class stationSpider(network.networkRBSpider):
    name = "rb-bremen1"
    station = "Bremen Eins"
    start_urls = ['https://www.bremeneins.de/suche/titelsuche-112.html']

    def get_loop(self, response):
        return response.css('tr')

    def get_date(self, response, item, counter):
        return response.css('#playlistsearch-searchDate::attr(value)').extract_first()

    def get_time(self, response, item, counter):
        return item.css("td:nth-child(1) > div > span::text").extract_first()

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(2) > div::text').extract_first()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(3) > div::text').extract_first()    