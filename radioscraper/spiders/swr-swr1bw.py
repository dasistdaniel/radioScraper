import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr1rp"
    station = "SWR1"
    start_urls = ['https://www.swr.de/~webradio/swr1/rp/swr1rp-playerbar-100~playerbarContainer.json']