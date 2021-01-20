import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4hn"
    station = "SWR4 Heilbronn"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/heilbronn/swr4hn-playerbar-100~playerbarContainer.json']