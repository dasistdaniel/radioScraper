import radioscraper.spiders.baseSpiders.baseRBB as network

class stationSpider(network.networkRBBSpider):
    name = "rbb-antennebrandenburg"
    station = "rbb Antenne Brandenburg"
    start_urls = ['http://playlisten.rbb-online.de/antenne_brandenburg/main/index.php']