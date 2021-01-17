import radioscraper.spiders.baseSpiders.baseRBB as rbb

class rbbSpider(rbb.rbbSpider):
    name = "rbb-antennebrandenburg"
    station = "rbb Antenne Brandenburg"
    start_urls = ['http://playlisten.rbb-online.de/antenne_brandenburg/main/index.php']