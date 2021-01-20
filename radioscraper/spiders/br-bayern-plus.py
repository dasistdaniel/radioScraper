import radioscraper.spiders.baseSpiders.baseBR as network

class stationSpider(network.networkBRSpider):
    name = "br-bayernplus"
    station = "Bayern plus"
    start_urls = ['https://www.br.de/radio/bayern-plus/welle118.html']