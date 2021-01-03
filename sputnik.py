import baseSpiders.mdr as mdr

class sputnikSpider(mdr.mdrSpider):
    name = "sputnik"
    start_urls = ['https://www.sputnik.de/xaps2/frontend/utils/titellistenproxy/data?amount=10']
