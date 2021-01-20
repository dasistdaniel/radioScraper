import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4tr"
    station = "SWR4 Trier"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/trier/trier-playerbar-100~playerbarContainer.json']