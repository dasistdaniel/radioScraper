import baseSpiders.wdr as wdr

class cosmoSpider(wdr.wdrSpider):
    name = "cosmo"
    start_urls = ['https://www1.wdr.de/radio/cosmo/musik/playlist/index.html']