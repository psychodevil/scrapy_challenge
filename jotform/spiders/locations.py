import scrapy
from ..items import JotformItem


class LocationsSpider(scrapy.Spider):
    name = 'locations'
    start_urls = ['https://londonrelocation.com/properties-to-rent/']

    def parse(self, response):
        items = JotformItem()
        location = [i for i in response.css('.stick-bottom a').xpath('@href').extract() if '?' in i]
        items['location'] = location
        yield items
