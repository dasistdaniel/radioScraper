import baseSpiders.ndr as ndr

class ndrblueSpider(ndr.ndrSpider):
    name = "ndrblue"
    start_urls = ['https://www.ndr.de/ndrblue/programm/titelliste1214.html']