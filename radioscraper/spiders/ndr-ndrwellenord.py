import radioscraper.spiders.baseSpiders.baseNDR as network

class stationSpider(network.networkNDRSpider):
    name = "ndr-ndrwellenord"
    station = "NDR Welle Nord"
    start_urls = ['https://www.ndr.de/wellenord/programm/titelliste1204.html']