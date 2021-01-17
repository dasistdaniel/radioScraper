import radioscraper.spiders.baseSpiders.baseMDR as mdr

class mdrsachsenSpider(mdr.mdrSpider):
    name = "mdr-mdrsachsen"
    station = "MDR Sachsen"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=4&amount=10']