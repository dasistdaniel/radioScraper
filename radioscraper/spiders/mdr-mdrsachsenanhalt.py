import radioscraper.spiders.baseSpiders.baseMDR as mdr

class mdrsachsenanhaltSpider(mdr.mdrSpider):
    name = "mdr-mdrsachsenanhalt"
    station = "MDR Sachsen-Anhalt"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=5&amount=10']