import radioscraper.spiders.baseSpiders.baseMDR as network

class stationSpider(network.networkMDRSpider):
    name = "mdr-mdrkultur"
    station = "MDR Kultur"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=8&amount=10']