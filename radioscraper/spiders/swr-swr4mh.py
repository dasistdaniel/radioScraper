import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4mh"
    station = "SWR4 Mannheim"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/mannheim/mannheim-playerbar-100~playerbarContainer.json']