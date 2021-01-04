import baseSpiders.ndr as ndr

class ndrplusSpider(ndr.ndrSpider):
    name = "ndrplus"
    start_urls = ['https://www.ndr.de/ndrplus/programm/titelliste1230.html']