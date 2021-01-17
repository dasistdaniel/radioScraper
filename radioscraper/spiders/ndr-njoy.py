import radioscraper.spiders.baseSpiders.baseNDR as ndr

class njoySpider(ndr.ndrSpider):
    name = "ndr-njoy"
    station = "N-Joy"
    start_urls = ['https://www.n-joy.de/musik/titelliste/index.html']