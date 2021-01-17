import baseSpiders.rb as rb

class bremennextSpider(rb.rbSpider):
    name = "bremen next"
    start_urls = ['https://www.radiobremen.de/bremennext/titelsuche/']

    def get_loop(self, response):
        return response.css('.titelsuche>ul>li')
    
    def get_date(self, response, item, counter):
        return self.gerdatetoiso(response.css("#titelsuche-form > div:nth-child(1) > div > select > option:nth-child(1)::attr(value)").extract_first())
    
    def get_time(self, response, item, counter):
        return item.css(".tracktime::text").extract_first() + ":00"

    def get_artist(self, response, item, counter):
        artist = item.css("::text")[1].extract().split(':')[0].strip().lower().replace(' mit ', ' feat. ')
        return artist

    def get_title(self, response, item, counter):
        title = item.css("::text")[1].extract().split(':')[1].strip().lower()
        return title
