import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndr1mv"
    station = "NDR1 Mecklenburg-Vorpommern"
    start_urls = ['https://www.ndr.de/radiomv/programm/titelliste1206.html']