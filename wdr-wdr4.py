import baseSpiders.wdr as wdr

class wdr4Spider(wdr.wdrSpider):
    name = "wdr4"
    start_urls = ['https://www1.wdr.de/radio/wdr4/titelsuche-wdrvier-102.html']