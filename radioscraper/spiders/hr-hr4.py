import radioscraper.spiders.baseSpiders.baseHR as network

class stationSpider(network.networkHRSpider):
    name = "hr-hr4"
    station ="HR4"
    start_urls = ['https://www.hr4.de/musik/titelliste/playlist_hrfour-100.html']