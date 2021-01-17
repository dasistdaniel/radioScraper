import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndr2Spider(ndr.ndrSpider):
    name = "ndr-ndr2"
    station = "NDR2"
    start_urls = ['https://www.ndr.de/ndr2/programm/titelliste1202.html']