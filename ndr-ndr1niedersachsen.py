import baseSpiders.ndr as ndr

class ndr1niedersachsenSpider(ndr.ndrSpider):
    name = "ndr1-niedersachsen"
    start_urls = ['https://www.ndr.de/ndr1niedersachsen/programm/titelliste1210.html']