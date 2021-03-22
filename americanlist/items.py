import scrapy


class Bank(scrapy.Item):
    name = scrapy.Field()
    locations = scrapy.Field()
    hq = scrapy.Field()
    website = scrapy.Field()
