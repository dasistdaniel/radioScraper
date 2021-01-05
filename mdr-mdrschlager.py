import baseSpiders.mdr as mdr

class mdrschlagerSpider(mdr.mdrSpider):
    name = "mdr-schlager"
    start_urls = ['https://www.sputnik.de/xaps2/frontend/utils/titellistenproxy/data?amount=10']
