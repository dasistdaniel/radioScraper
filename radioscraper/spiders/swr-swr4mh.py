import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4mh"
    station = "SWR4 Mannheim"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/mannheim/mannheim-playerbar-100~playerbarContainer.json']