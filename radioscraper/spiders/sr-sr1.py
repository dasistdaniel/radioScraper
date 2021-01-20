import radioscraper.spiders.baseSpiders.baseSR as network

class stationSpider(network.networkSRSpider):
    name = "sr-sr1"
    station = "SR1"
    start_urls = ['https://musikrecherche.sr.de/sr1sophora/musicresearch.php']