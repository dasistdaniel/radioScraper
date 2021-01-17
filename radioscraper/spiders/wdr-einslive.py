import radioscraper.spiders.baseSpiders.baseWDR as wdr

class einsliveSpider(wdr.wdrSpider):
    name = "wdr-einslive"
    station = "EinsLive"
    start_urls = ['https://www1.wdr.de/radio/1live/on-air/1live-playlist/index.html']