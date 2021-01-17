import baseSpiders.rb as rb
import datetime
import locale

class bremen4Spider(rb.rbSpider):
    name = "bemen vier"
    start_urls = ['https://www.bremenvier.de/programm/titelsuche-100.html']

    def get_loop(self, response):
        return response.css('.-table-playlist>tbody>tr')

    def get_date(self, response, item, counter):
        return response.css('#playlistsearch-searchDate::attr(value)').extract_first()

    def get_time(self, response, item, counter):
        return item.css("td:nth-child(1)>div>span::text").extract_first() + ":00"

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(2)>div::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(3)>div::text').extract_first().strip().lower()    