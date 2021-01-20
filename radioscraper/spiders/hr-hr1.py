import radioscraper.spiders.baseSpiders.baseHR as network

class stationSpider(network.networkHRSpider):
    name = "hr-hr1"
    station = "HR1"
    start_urls = ['https://www.hr1.de/musik/titelliste/index.html']