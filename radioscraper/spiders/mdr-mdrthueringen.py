import radioscraper.spiders.baseSpiders.baseMDR as mdr

class mdrthueringenSpider(mdr.mdrSpider):
    name = "mdr-mdrthueringen"
    station = "MDR Thüringen"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=6&amount=10']