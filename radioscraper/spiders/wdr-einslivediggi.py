import radioscraper.spiders.baseSpiders.baseWDR as network

class stationSpider(network.networkWDRSpider):
    name = "wdr-einslive-diggi"
    station = "EinsLive diggi"
    start_urls = ['https://www1.wdr.de/radio/1live-diggi/onair/1live-diggi-playlist/index.html']