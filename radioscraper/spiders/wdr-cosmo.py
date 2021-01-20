import radioscraper.spiders.baseSpiders.baseWDR as network

class stationSpider(network.networkWDRSpider):
    name = "wdr-cosmo"
    station = "cosmo"
    start_urls = ['https://www1.wdr.de/radio/cosmo/musik/playlist/index.html']