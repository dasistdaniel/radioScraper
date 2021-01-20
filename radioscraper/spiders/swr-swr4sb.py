import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4sb"
    station = "SWR4 Südbaden"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/suedbaden/suedbaden-playerbar-100~playerbarContainer.json']