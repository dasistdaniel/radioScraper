import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4lh"
    station = "SWR4 Ludwigshafen"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/ludwigshafen/ludwigshafen-playerbar-100~playerbarContainer.json']