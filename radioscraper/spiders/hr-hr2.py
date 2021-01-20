import radioscraper.spiders.baseSpiders.baseHR as network

class stationSpider(network.networkHRSpider):
    name = "hr-hr2"
    station = "HR2"
    start_urls = ['https://www.hr2.de/programm/hrzwei-playlist-100.html']