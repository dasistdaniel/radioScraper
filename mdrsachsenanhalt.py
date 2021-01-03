import baseSpiders.mdr as mdr

class mdrsachsenanhaltSpider(mdr.mdrSpider):
    name = "mdrsachsenanhalt"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=5&amount=10']
