import scrapy
import json

class baseSpider(scrapy.Spider):
    def parse(self, response):
        playlist = []
        loop = self.get_loop(response)
        for item in loop:
            date = self.get_date(response,item)
            time = self.get_time(response,item)
            artist = self.get_artist(response,item)
            title = self.get_title(response,item)
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title})

        output = {
            'name': self.name, 
            'url': self.start_urls[0],
            'result': playlist
        }

        #print(output)
        print(json.dumps(output,indent=4,ensure_ascii=False))
