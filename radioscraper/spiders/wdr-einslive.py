import radioscraper.spiders.baseSpiders.baseWDR as network

class stationSpider(network.networkWDRSpider):
    name = "wdr-einslive"
    station = "EinsLive"
    start_urls = ['https://www1.wdr.de/radio/1live/on-air/1live-playlist/index.html']