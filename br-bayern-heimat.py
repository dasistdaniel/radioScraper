import baseSpiders.br as br

class brheimatSpider(br.brSpider):
    name = "bayern-heimat"
    start_urls = ['https://www.br.de/radio/br-heimat/welle128.html']
