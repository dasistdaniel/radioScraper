import radioscraper.spiders.baseSpiders.baseWDR as wdr

class einslivediggiSpider(wdr.wdrSpider):
    name = "wdr-einslive-diggi"
    station = "EinsLive diggi"
    start_urls = ['https://www1.wdr.de/radio/1live-diggi/onair/1live-diggi-playlist/index.html']