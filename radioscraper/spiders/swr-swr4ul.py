import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4ul"
    station = "SWR4 Ulm"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/ulm/ulm-playerbar-100~playerbarContainer.json']