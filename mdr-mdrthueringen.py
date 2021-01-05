import baseSpiders.mdr as mdr

class mdrthueringenSpider(mdr.mdrSpider):
    name = "mdr-thueringen"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=6&amount=10']
