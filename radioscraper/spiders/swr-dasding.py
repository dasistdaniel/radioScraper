import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-dasding"
    station = "Das Ding"
    start_urls = ['https://www.dasding.de/~webradio/administration/playerbar/dasding-playerbar-100~playerbarContainer.json']