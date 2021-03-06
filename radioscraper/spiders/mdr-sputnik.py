import json
import radioscraper.spiders.baseSpiders.baseMDR as network

class stationSpider(network.networkMDRSpider):
    name = "mdr-sputnik"
    station = "Sputnik"
    start_urls = ['https://www.sputnik.de/xaps2/frontend/utils/titellistenproxy/data?amount=10']

    def get_date(self, response, item, counter):
        return self.gerdatetoiso(json.loads(response.text)["Songs"][item]["starttime"][-10:])
    
    def get_time(self, response, item, counter):
        return json.loads(response.text)["Songs"][item]["starttime"][0:5]