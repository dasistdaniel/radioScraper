import radioscraper.spiders.baseSpiders.baseSpider as base
import json

class networkMDRSpider(base.baseSpider):
    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }

    network = 'mdr'
    def get_loop(self, response):
        return json.loads(response.text)['Songs']
    
    def get_date(self, response, item, counter):        
        return json.loads(response.text)["Songs"][item]["starttime"][0:10]
    
    def get_time(self, response, item, counter):
        return json.loads(response.text)["Songs"][item]["starttime"][-8:]

    def get_artist(self, response, item, counter):
        return json.loads(response.text)["Songs"][item]["interpret"]

    def get_title(self, response, item, counter):
        return json.loads(response.text)["Songs"][item]["title"]
