import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4kl"
    station = "SWR4 Kaiserslautern"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/kaiserslautern/swr4kl-playerbar-100~playerbarContainer.json']