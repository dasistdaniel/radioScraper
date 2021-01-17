import radioscraper.spiders.baseSpiders.baseWDR as wdr

class wdr2Spider(wdr.wdrSpider):
    name = "wdr-wdr2"
    station = "WDR2"
    start_urls = ['https://www1.wdr.de/radio/wdr2/musik/playlist/index.html']