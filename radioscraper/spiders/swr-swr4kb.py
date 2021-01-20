import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr4kb"
    station = "SWR4 Koblenz"
    start_urls = ['https://www.swr.de/~webradio/swr4/nachrichten/koblenz/koblenz-playerbar-100~playerbarContainer.json']