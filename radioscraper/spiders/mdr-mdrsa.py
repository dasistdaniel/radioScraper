import radioscraper.spiders.baseSpiders.baseMDR as network

class stationSpider(network.networkMDRSpider):
    name = "mdr-mdrsa"
    station = "MDR Sachsen-Anhalt"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=5&amount=10']