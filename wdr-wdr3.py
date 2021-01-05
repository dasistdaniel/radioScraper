import baseSpiders.wdr as wdr

class wdr3Spider(wdr.wdrSpider):
    name = "wdr3"
    start_urls = ['https://www1.wdr.de/radio/wdr3/titelsuche-wdrdrei-104.html']