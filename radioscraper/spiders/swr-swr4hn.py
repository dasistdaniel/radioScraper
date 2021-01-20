import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4hn"
    station = "SWR4 Heilbronn"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/heilbronn/swr4hn-playerbar-100~playerbarContainer.json']