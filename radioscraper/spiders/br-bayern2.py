import radioscraper.spiders.baseSpiders.baseBR as network

class stationSpider(network.networkBRSpider):
    name = "br-bayern2"
    station = "Bayern 2"
    start_urls = ['https://www.br.de/radio/bayern2/welle106.html']