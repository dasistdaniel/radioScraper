import radioscraper.spiders.baseSpiders.baseBR as network

class stationSpider(network.networkBRSpider):
    name = "br-puls"
    station = "Puls"
    start_urls = ['https://www.br.de/puls/welle116.html']

    def get_artist(self, response, item, counter):
        data = item.css('ul > li > span:nth-child(1)::text').extract_first().strip().lower()
        if data != 'puls':
            return data
        else:
            return None