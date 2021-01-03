import baseSpiders.wdr as wdr

class wdr5Spider(wdr.wdrSpider):
    name = "wdr5"
    start_urls = ['https://www1.wdr.de/radio/wdr5/musik/titelsuche-wdrfuenf-104.html']