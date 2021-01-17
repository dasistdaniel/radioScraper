import radioscraper.spiders.baseSpiders.baseSR as sr

class sr1Spider(sr.srSpider):
    name = "sr-sr1"
    station = "SR1"
    start_urls = ['https://musikrecherche.sr.de/sr1sophora/musicresearch.php']