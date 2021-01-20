import radioscraper.spiders.baseSpiders.baseSWR as network

class stationSpider(network.networkSWRSpider):
    name = "swr-swr4rp"
    station = "SWR4 Rheinland-Pfalz"
    start_urls = ['https://www.swr.de/~webradio/swr4/programm-rp/swr4rp-playerbar-100~playerbarContainer.json']