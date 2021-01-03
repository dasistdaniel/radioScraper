import baseSpiders.wdr as wdr

class wdr2Spider(wdr.wdrSpider):
    name = "wdr2"
    start_urls = ['https://www1.wdr.de/radio/wdr2/musik/playlist/index.html']