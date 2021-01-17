import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndrkulturSpider(ndr.ndrSpider):
    name = "ndr-ndrkultur"
    station = "NDR Kultur"
    start_urls = ['https://www.ndr.de/ndrkultur/programm/titelliste1212.html']