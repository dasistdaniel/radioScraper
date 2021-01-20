import radioscraper.spiders.baseSpiders.baseSR as network

class stationSpider(network.networkSRSpider):
    name = "sr-sr2"
    station = "SR2"
    start_urls = ['https://musikrecherche.sr.de/sr2sophora/musicresearch.php']

    def get_loop(self, response):
        return response.css('.musicResearch__Item:nth-child(n+3)')    