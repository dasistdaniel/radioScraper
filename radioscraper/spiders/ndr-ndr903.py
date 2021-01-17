import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndr903Spider(ndr.ndrSpider):
    name = "ndr-ndr903"
    station = "NDR 90.3"
    start_urls = ['https://www.ndr.de/903/programm/titelliste1208.html']