import baseSpiders.mdr as mdr

class mdrkulturSpider(mdr.mdrSpider):
    name = "mdr-kultur"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=8&amount=10']
