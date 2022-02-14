# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JotformItem(scrapy.Item):
    # define the fields for your item here like:
    title        = scrapy.Field()
    price        = scrapy.Field()
    property_url = scrapy.Field()
    location     = scrapy.Field()
