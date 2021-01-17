import radioscraper.spiders.baseSpiders.baseWDR as wdr

class wdr5Spider(wdr.wdrSpider):
    name = "wdr-wdr5"
    station = "WDR5"
    start_urls = ['https://www1.wdr.de/radio/wdr5/musik/titelsuche-wdrfuenf-104.html']