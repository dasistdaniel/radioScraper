import radioscraper.spiders.baseSpiders.baseSR as sr

class sr3Spider(sr.srSpider):
    name = "sr-sr3"
    station = "SR3"
    start_urls = ['https://musikrecherche.sr.de/sr3sophora/musicresearch.php']

    #def get_loop(self, response):
    #    return response.css('.musicResearch__Item:nth-child(n+3)')    