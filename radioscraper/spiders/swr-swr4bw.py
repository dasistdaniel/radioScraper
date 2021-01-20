import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4bw"
    station = "SWR4 Baden Würtemberg"
    start_urls = ['https://www.swr.de/~webradio/swr4/swr4bw-playerbar-100~playerbarContainer.json']