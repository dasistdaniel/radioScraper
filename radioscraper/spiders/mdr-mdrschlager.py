import radioscraper.spiders.baseSpiders.baseMDR as network

class stationSpider(network.networkMDRSpider):
    name = "mdr-mdrschlager"
    station = "MDR Schlager"
    start_urls = ['https://www.mdr.de/scripts4/titellisten/xmlresp-index.do?output=json&idwelle=22&amount=10']