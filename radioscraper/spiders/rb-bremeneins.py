import radioscraper.spiders.baseSpiders.baseRB as rb
import datetime

class bremen1Spider(rb.rbSpider):
    d = datetime.datetime.now()
    name = "rb-bremen1"
    station = "Bremen Eins"
    start_urls = [f'https://www.radiobremen.de/bremeneins/musik/titelsuche/?wrapurl=%2Fbremeneins%2Fmusik%2Ftitelsuche%2F&selectdate={d.strftime("%Y-%m-%d")}&stunde={d.hour:02}&minute={int(d.minute / 15) * 15:02}']