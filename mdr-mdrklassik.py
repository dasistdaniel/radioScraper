import baseSpiders.mdr as mdr

class mdrklassikSpider(mdr.mdrSpider):
    name = "mdr-klassik"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=7&amount=10']
