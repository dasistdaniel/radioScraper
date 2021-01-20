import radioscraper.spiders.baseSpiders.baseBR as network

class stationSpider(network.networkBRSpider):
    name = "br-bayern1"
    station = "Bayern 1"
    start_urls = ['https://www.br.de/radio/bayern-1/welle110.html']