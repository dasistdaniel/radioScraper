import baseSpiders.mdr as mdr

class mdrschlagerSpider(mdr.mdrSpider):
    name = "mdr-schlager"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=22&amount=10']
