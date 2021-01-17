import radioscraper.spiders.baseSpiders.baseNDR as ndr

class ndr1niedersachsenSpider(ndr.ndrSpider):
    name = "ndr-ndr1niedersachsen"
    station = "NDR1 Niedersachsen"
    start_urls = ['https://www.ndr.de/ndr1niedersachsen/programm/titelliste1210.html']