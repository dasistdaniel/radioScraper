import radioscraper.spiders.baseSpiders.baseMDR as mdr

class jumpSpider(mdr.mdrSpider):
    name = "mdr-jump"
    station = "Jump"
    start_urls = ['https://www.mdr.de/XML/titellisten/jump_onair.json?json']