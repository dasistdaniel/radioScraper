import baseSpiders.ndr as ndr

class ndr2Spider(ndr.ndrSpider):
    name = "ndr2"
    start_urls = ['https://www.ndr.de/ndr2/programm/titelliste1202.html']