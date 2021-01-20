import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndrplus"
    station = "NDR Plus"
    start_urls = ['https://www.ndr.de/ndrplus/programm/titelliste1230.html']