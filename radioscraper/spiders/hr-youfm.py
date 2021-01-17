import radioscraper.spiders.baseSpiders.baseHR as hr

class youfmSpider(hr.hrSpider):
    name = "hr-youfm"
    station = "youfm"
    start_urls = ['https://www.you-fm.de/playlists/was-lief-wann/playlist_you-fm-100.html']