import radioscraper.spiders.baseSpiders.baseSpider as base

class networkRBSpider(base.baseSpider):
    network = 'rb'
    def get_loop(self, response):
        return response.css('tr:not(:first-child)')

    def get_date(self, response, item, counter):
        return response.css('#titelsuche > div:nth-child(2) > select > option:nth-child(1)::attr(value)').extract_first().strip()

    def get_time(self, response, item, counter):
        return item.css("td:nth-child(1)::text").extract_first()

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(2)::text').extract_first()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(3)::text').extract_first()