import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4sg"
    station = "SWR4 Stuttgart"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/stuttgart/stuttgart-playerbar-100~playerbarContainer.json']