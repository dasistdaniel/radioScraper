import radioscraper.spiders.baseSpiders.baseRBB as network

class stationSpider(network.networkRBBSpider):
    name = "rbb-rbb888"
    station = "rbb 88.8"
    start_urls = ['http://playlisten.rbb-online.de/rbb888/main/index.php']