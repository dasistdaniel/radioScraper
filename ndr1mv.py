import baseSpiders.ndr as ndr

class ndr1mvSpider(ndr.ndrSpider):
    name = "ndr1mv"
    start_urls = ['https://www.ndr.de/radiomv/programm/titelliste1206.html']