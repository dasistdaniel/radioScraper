import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4kl"
    station = "SWR4 Kaiserslautern"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/kaiserslautern/swr4kl-playerbar-100~playerbarContainer.json']