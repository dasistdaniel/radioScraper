import baseSpiders.ndr as ndr

class ndrkulturSpider(ndr.ndrSpider):
    name = "ndrkultur"
    start_urls = ['https://www.ndr.de/ndrkultur/programm/titelliste1212.html']