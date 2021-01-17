import radioscraper.spiders.baseSpiders.baseRB as rb
import datetime
import locale

class bremen2Spider(rb.rbSpider):
    name = "rb-bremen2"
    station = "Bremen Zwei"

    d = datetime.datetime.now()
    start_urls = [f'https://www.bremenzwei.de/musik/titelsuche-106~ajax.html?playlistsearch-searchDate={d.strftime("%Y-%m-%d")}&playlistsearch-searchTime={d.hour:02}%3A{int(d.minute / 15) * 15:02}']

    def get_loop(self, response):
        return response.css('tr.playlistsearch-rowtype-default')
    
    def get_date(self, response, item, counter):
        locale.setlocale(locale.LC_ALL, 'de_DE')
        date_string = response.css("h3::text").extract()[1].strip()
        date = datetime.datetime.strptime(date_string, '%d. %B %Y,')
        return date.strftime("%Y-%m-%d")
    
    def get_time(self, response, item, counter):
        return item.css("td:nth-child(1)>span::text").extract_first()# + ":00"

    def get_artist(self, response, item, counter):
        return item.css('td:nth-child(2)::text').extract_first().strip().lower()

    def get_title(self, response, item, counter):
        return item.css('td:nth-child(3)::text').extract_first().strip().lower()