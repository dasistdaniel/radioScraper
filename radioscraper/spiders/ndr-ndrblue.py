import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndrblue"
    station = "NDR Blue"
    start_urls = ['https://www.ndr.de/ndrblue/programm/titelliste1214.html']