import radioscraper.spiders.baseSpiders.baseWDR as wdr

class cosmoSpider(wdr.wdrSpider):
    name = "wdr-cosmo"
    station = "cosmo"
    start_urls = ['https://www1.wdr.de/radio/cosmo/musik/playlist/index.html']