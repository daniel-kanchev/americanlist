import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from americanlist.items import Bank


class ListSpider(scrapy.Spider):
    name = 'list'
    start_urls = ['https://www.bankbranchlocator.com/banks-in-usa.html']

    def parse(self, response):
        letters = response.xpath('//div[@class="content"]/div[3]/div[2]/a/@href').getall()
        yield from response.follow_all(letters, self.parse_letters)

    def parse_letters(self, response):
        banks = response.xpath('//ul[@class="listing"]/li//div[@class="bankinfoimage"]/a/@href').getall()
        yield from response.follow_all(banks, self.parse_banks)

    def parse_banks(self, response):
        item = ItemLoader(Bank())
        item.default_output_processor = TakeFirst()

        name = response.xpath('//ul[@class="details"]/li[1]//span[@class="dvalue"]/text()').get()
        locations = response.xpath('//ul[@class="details"]/li[5]//span[@class="dvalue"]/text()').get()
        website = response.xpath('//ul[@class="details"]/li[6]//span[@class="dvalue"]/a/@href').get()
        hq = response.xpath('//span[@class="dvaluex"]/text()').get()

        item.add_value('name', name)
        item.add_value('locations', locations)
        item.add_value('hq', hq)
        item.add_value('website', website)

        return item.load_item()
