import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4bw"
    station = "SWR4 Baden Würtemberg"
    start_urls = ['https://www.swr.de/~webradio/swr4/swr4bw-playerbar-100~playerbarContainer.json']