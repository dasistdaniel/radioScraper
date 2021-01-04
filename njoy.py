import baseSpiders.ndr as ndr

class njoySpider(ndr.ndrSpider):
    name = "njoy"
    start_urls = ['https://www.n-joy.de/musik/titelliste/index.html']