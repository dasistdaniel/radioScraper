import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4mz"
    station = "SWR4 Mainz"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/mainz/swr4mz-playerbar-100~playerbarContainer.json']