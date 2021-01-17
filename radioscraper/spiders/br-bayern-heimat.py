import radioscraper.spiders.baseSpiders.baseBR as br

class brheimatSpider(br.brSpider):
    name = "br-bayern-heimat"
    station = "Bayern Heimat"
    start_urls = ['https://www.br.de/radio/br-heimat/welle128.html']