import radioscraper.spiders.baseSpiders.baseHR as network

class stationSpider(network.networkHRSpider):
    name = "hr-youfm"
    station = "youfm"
    start_urls = ['https://www.you-fm.de/playlists/was-lief-wann/playlist_you-fm-100.html']