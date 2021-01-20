import radioscraper.spiders.baseSpiders.baseSpider as base
import json

class swrSpider(base.baseSpider):
    network = 'swr'

    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    def get_loop(self, response):
        return json.loads(response.text)['playlist']['data']
    
    def get_date(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["starttime"]
    
    def get_time(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["starttime"]

    def get_artist(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["artist"]

    def get_title(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["title"]


