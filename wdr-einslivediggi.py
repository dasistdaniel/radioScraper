import baseSpiders.wdr as wdr

class einslivediggiSpider(wdr.wdrSpider):
    name = "einslive-diggi"
    start_urls = ['https://www1.wdr.de/radio/1live-diggi/onair/1live-diggi-playlist/index.html']