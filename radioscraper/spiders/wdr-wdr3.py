import radioscraper.spiders.baseSpiders.baseWDR as wdr

class wdr3Spider(wdr.wdrSpider):
    name = "wdr-wdr3"
    station = "WDR3"
    start_urls = ['https://www1.wdr.de/radio/wdr3/titelsuche-wdrdrei-104.html']