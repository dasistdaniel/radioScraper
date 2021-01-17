# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RadioscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    station = scrapy.Field()
    network = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
