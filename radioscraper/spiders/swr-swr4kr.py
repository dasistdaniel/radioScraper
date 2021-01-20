import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4kr"
    station = "SWR4 Karlsruhe"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/karlsruhe/karlsruhe-playerbar-100~playerbarContainer.json']