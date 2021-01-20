import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4tb"
    station = "SWR4 Tübingen"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/tuebingen/tuebingen-playerbar-100~playerbarContainer.json']