import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndr903"
    station = "NDR 90.3"
    start_urls = ['https://www.ndr.de/903/programm/titelliste1208.html']