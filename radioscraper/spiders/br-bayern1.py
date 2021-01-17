import radioscraper.spiders.baseSpiders.baseBR as br

class bayern1Spider(br.brSpider):
    name = "br-bayern1"
    station = "Bayern 1"
    start_urls = ['https://www.br.de/radio/bayern-1/welle110.html']