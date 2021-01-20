import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr3"
    station = "SWR3"
    start_urls = ['https://www.swr.de/~webradio/administration/playerbar-swr3/swr3-playerbar-100~playerbarContainer.json']