import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4sg"
    station = "SWR4 Stuttgart"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/stuttgart/stuttgart-playerbar-100~playerbarContainer.json']