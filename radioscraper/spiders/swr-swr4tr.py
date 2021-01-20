import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4tr"
    station = "SWR4 Trier"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/trier/trier-playerbar-100~playerbarContainer.json']