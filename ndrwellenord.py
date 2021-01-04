import baseSpiders.ndr as ndr

class ndrwellenordSpider(ndr.ndrSpider):
    name = "ndrwellenord"
    start_urls = ['https://www.ndr.de/wellenord/programm/titelliste1204.html']