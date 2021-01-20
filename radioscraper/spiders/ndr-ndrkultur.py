import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndrkultur"
    station = "NDR Kultur"
    start_urls = ['https://www.ndr.de/ndrkultur/programm/titelliste1212.html']