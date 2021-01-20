import radioscraper.spiders.baseSpiders.baseMDR as network

class stationSpider(network.networkMDRSpider):
    name = "mdr-jump"
    station = "Jump"
    start_urls = ['https://www.mdr.de/XML/titellisten/jump_onair.json?json']