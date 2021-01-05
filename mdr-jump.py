import baseSpiders.mdr as mdr

class jumpSpider(mdr.mdrSpider):
    name = "jump"
    start_urls = ['https://www.mdr.de/XML/titellisten/jump_onair.json?json']
