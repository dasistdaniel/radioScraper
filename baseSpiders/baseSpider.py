import scrapy
import json

class baseSpider(scrapy.Spider):
    def parse(self, response):
        playlist = []
        loop = self.get_loop(response)
        for item in loop:
            date = self.get_date(item)
            time = self.get_time(item)
            artist = self.get_artist(item)
            title = self.get_title(item)
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title})

        output = {
            'name': self.name, 
            'url': self.start_urls[0],
            'result': playlist
        }

        #print(output)
        print(json.dumps(output,indent=4,ensure_ascii=False))
