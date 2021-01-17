import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndr1mvSpider(ndr.ndrSpider):
    name = "ndr-ndr1mv"
    station = "NDR1 Mecklenburg-Vorpommern"
    start_urls = ['https://www.ndr.de/radiomv/programm/titelliste1206.html']