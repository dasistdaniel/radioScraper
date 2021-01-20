import radioscraper.spiders.baseSpiders.baseWDR as network

class stationSpider(network.networkWDRSpider):
    name = "wdr-wdr4"
    station = "WDR4"
    start_urls = ['https://www1.wdr.de/radio/wdr4/titelsuche-wdrvier-102.html']