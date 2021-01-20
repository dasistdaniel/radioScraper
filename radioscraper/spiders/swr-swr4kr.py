import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4kr"
    station = "SWR4 Karlsruhe"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/karlsruhe/karlsruhe-playerbar-100~playerbarContainer.json']