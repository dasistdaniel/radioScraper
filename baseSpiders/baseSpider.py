import scrapy
import json

class baseSpider(scrapy.Spider):
    def parse(self, response):
        playlist = []
        loop = self.get_loop(response)
        counter = 0
        for item in loop:
            date = self.get_date(response,item, counter)
            time = self.get_time(response,item, counter)
            artist = self.get_artist(response,item, counter)
            title = self.get_title(response,item, counter)
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title})
            counter = counter + 1

        output = {
            'name': self.name, 
            'url': self.start_urls[0],
            'result': playlist
        }

        #print(output)
        print(json.dumps(output,indent=4,ensure_ascii=False))
