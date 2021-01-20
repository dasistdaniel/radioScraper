import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4kb"
    station = "SWR4 Koblenz"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/koblenz/koblenz-playerbar-100~playerbarContainer.json']