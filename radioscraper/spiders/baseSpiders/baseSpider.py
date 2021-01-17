import scrapy
import json

class baseSpider(scrapy.Spider):
    def gerdatetoiso(self, date):
        dateparts = date.split('.')
        newdate = f"{dateparts[2]}-{dateparts[1]}-{dateparts[0]}"
        return newdate

    def parse(self, response):
        #playlist = []
        loop = self.get_loop(response)
        counter = 0
        for item in loop:
            date = self.get_date(response, item, counter)
            time = self.get_time(response, item, counter)
            artist = self.get_artist(response, item, counter)
            title = self.get_title(response, item, counter)
            if date != None and time != None and artist != None and title != None:
                yield {
                    'network': self.network,
                    'station': self.station,
                    'date': date,
                    'time': time,
                    'artist': artist,
                    'title': title,
                } 
                counter = counter + 1