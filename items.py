# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZooplaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    seller = scrapy.Field()
    phone = scrapy.Field()
    bedrooms = scrapy.Field()
    toilets = scrapy.Field()
    chairs = scrapy.Field()
    date_listed = scrapy.Field()
    url = scrapy.Field()




    pass
