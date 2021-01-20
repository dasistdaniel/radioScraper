import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4tb"
    station = "SWR4 Tübingen"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/tuebingen/tuebingen-playerbar-100~playerbarContainer.json']