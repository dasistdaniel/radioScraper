import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndr1niedersachsen"
    station = "NDR1 Niedersachsen"
    start_urls = ['https://www.ndr.de/ndr1niedersachsen/programm/titelliste1210.html']