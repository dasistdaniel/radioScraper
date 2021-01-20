import json
import datetime
import radioscraper.spiders.baseSpiders.baseSpider as base

class networkSWRSpider(base.baseSpider):
    network = 'swr'

    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    def get_loop(self, response):
        return json.loads(response.text)['playlist']['data']
    
    def get_date(self, response, item, counter):
        timestamp = int(json.loads(response.text)["playlist"]['data'][counter]["starttime"])
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        return date
    
    def get_time(self, response, item, counter):
        timestamp = int(json.loads(response.text)["playlist"]['data'][counter]["starttime"])
        time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        return time

    def get_artist(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["artist"]

    def get_title(self, response, item, counter):
        return json.loads(response.text)["playlist"]['data'][counter]["title"]


