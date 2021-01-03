import baseSpiders.wdr as wdr

class einsliveSpider(wdr.wdrSpider):
    name = "einslive"
    start_urls = ['https://www1.wdr.de/radio/1live/on-air/1live-playlist/index.html']
