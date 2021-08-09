import scrapy
from scrapy_selenium import SeleniumRequest
from ..items import ZooplaItem

class ZoopSpider(scrapy.Spider):
    name = 'zoop'
    page_number = 2
    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.zoopla.co.uk/for-sale/property/london/?q=London&results_sort=newest_listings&search_source=home",
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        items = ZooplaItem()
        homes = response.xpath("//div[@data-testid='search-result']")
        for home in homes:
            items['title'] = home.xpath(".//a[@data-testid='listing-details-link']/h2/text()").get()
            items['address'] = home.xpath(".//a[@data-testid='listing-details-link']/p/text()").get()
            items['price'] = home.xpath(".//p[@class='css-6v9gpl-Text eczcs4p0']/text()").get()
            items['seller'] = home.xpath(".//a[@data-testid='listing-details-agent-logo']/img/@alt").get()
            if items['seller'] is not None:
                items['seller'] = items['seller'].strip('Marketed by ')
            items['phone'] = home.xpath(".//a[@data-testid='agent-phone-number']/text()").get()
            items['bedrooms'] = home.xpath(".//span[@data-testid='bed']/parent::span/following-sibling::p/text()").get()
            items['toilets'] = home.xpath(".//span[@data-testid='bath']/parent::span/following-sibling::p/text()").get()
            items['chairs'] = home.xpath(".//span[@data-testid='chair']/parent::span/following-sibling::p/text()").get()
            items['date_listed'] = home.xpath(".//span[@data-testid='date-published']/text()[3]").get()
            items['url'] = response.urljoin(home.xpath(".//a[@data-testid='listing-details-link']/@href").get())

            yield items

        next_page = f"https://www.zoopla.co.uk/for-sale/property/london/?page_size=25&q=London&radius=0&results_sort=newest_listings&pn={self.page_number}"
        if self.page_number < 400:
            self.page_number += 1
            yield SeleniumRequest(
                url=next_page,
                wait_time=3,
                callback=self.parse
            )