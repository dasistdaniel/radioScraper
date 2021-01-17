import radioscraper.spiders.baseSpiders.baseHR as hr

class hr1Spider(hr.hrSpider):
    name = "hr-hr1"
    station = "HR1"
    start_urls = ['https://www.hr1.de/musik/titelliste/index.html']