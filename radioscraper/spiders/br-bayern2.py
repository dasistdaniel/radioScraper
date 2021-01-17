import radioscraper.spiders.baseSpiders.baseBR as br

class bayern2Spider(br.brSpider):
    name = "br-bayern2"
    station = "Bayern 2"
    start_urls = ['https://www.br.de/radio/bayern2/welle106.html']