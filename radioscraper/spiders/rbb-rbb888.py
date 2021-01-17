import radioscraper.spiders.baseSpiders.baseRBB as rbb

class rbbSpider(rbb.rbbSpider):
    name = "rbb-rbb888"
    station = "rbb 88.8"
    start_urls = ['http://playlisten.rbb-online.de/rbb888/main/index.php']