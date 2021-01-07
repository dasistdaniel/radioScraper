import baseSpiders.ndr as ndr

class ndr903Spider(ndr.ndrSpider):
    name = "ndr-903"
    start_urls = ['https://www.ndr.de/903/programm/titelliste1208.html']