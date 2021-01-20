import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4fn"
    station = "SWR4 Friedrichshafen"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/friedrichshafen/swr4fn-playerbar-100~playerbarContainer.json']