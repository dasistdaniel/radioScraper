import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndrblueSpider(ndr.ndrSpider):
    name = "ndr-ndrblue"
    station = "NDR Blue"
    start_urls = ['https://www.ndr.de/ndrblue/programm/titelliste1214.html']