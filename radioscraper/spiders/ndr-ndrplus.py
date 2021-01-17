import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndrplusSpider(ndr.ndrSpider):
    name = "ndr-ndrplus"
    station = "NDR Plus"
    start_urls = ['https://www.ndr.de/ndrplus/programm/titelliste1230.html']