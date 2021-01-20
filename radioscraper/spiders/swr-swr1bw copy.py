import radioscraper.spiders.baseSpiders.baseSWR as swr

class swr1Spider(swr.swrSpider):
    name = "swr-swr1bw"
    station = "SWR1"
    start_urls = ['https://www.swr.de/~webradio/swr1/bw/swr1bw-playerbar-100~playerbarContainer.json']