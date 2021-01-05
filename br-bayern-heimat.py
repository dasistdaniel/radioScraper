import baseSpiders.br as br

class brheimatSpider(br.brSpider):
    name = "bayernheimat"
    start_urls = ['https://www.br.de/radio/br-heimat/welle128.html']
