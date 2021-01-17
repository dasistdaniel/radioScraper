import radioscraper.spiders.baseSpiders.baseBR as br

class brplusSpider(br.brSpider):
    name = "br-bayernplus"
    station = "Bayern plus"
    start_urls = ['https://www.br.de/radio/bayern-plus/welle118.html']