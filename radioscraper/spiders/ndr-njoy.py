import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-njoy"
    station = "N-Joy"
    start_urls = ['https://www.n-joy.de/musik/titelliste/index.html']