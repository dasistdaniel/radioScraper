import baseSpiders.mdr as mdr

class mdrsachsenSpider(mdr.mdrSpider):
    name = "mdr-sachsen"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=4&amount=10']
