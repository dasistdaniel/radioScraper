import radioscraper.spiders.baseSpiders.baseWDR as network

class stationSpider(network.networkWDRSpider):
    name = "wdr-wdr3"
    station = "WDR3"
    start_urls = ['https://www1.wdr.de/radio/wdr3/titelsuche-wdrdrei-104.html']