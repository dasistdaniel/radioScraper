import radioscraper.spiders.baseSpiders.baseHR as network

class stationSpider(network.networkHRSpider):
    name = "hr-hr3"
    station = "HR3"
    start_urls = ['https://www.hr3.de/musik/titelliste/playlist_hrthree-100.html']