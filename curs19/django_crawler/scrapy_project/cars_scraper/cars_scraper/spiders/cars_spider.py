import scrapy
from cars_scraper.items import CarItem

class CarsSpider(scrapy.Spider):
    name = 'cars'

    def start_requests(self):
        urls = [
            'https://999.md/ru/61630522',
            'https://999.md/ru/63698666',
            'https://999.md/ru/63588835'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split('/')[-1]
        # filename = 'cars-%s.html' % page

        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        yield {
            'title': response.xpath('//*[@id="container"]/div/section/header/h1/text()').get(),
            'price': response.xpath('//*[@id="container"]/div/section/div/div/div[4]/div/div/div/ul/li/span[1]/text()').get().strip(),
            'region': ''.join(response .css('.adPage__content__region dd::text ').getall()),
            'phones': response.xpath('//*[@id="container"]/div/section/div/div/div[4]/div/div/dl[2]/dd/ul/li[1]/a/@href').get()[4:]
        }


class CarsListSpider(scrapy.Spider):
    name = 'cars_list'
    start_urls = [
        'https://999.md/ru/list/transport/cars?view_type=detail'
    ]

    def parse(self, response):

        for car in response.css('.ads-list-detail-item'):
            item = CarItem()
            item['title'] = car.css('.ads-list-detail-item-title a::text').get()
            item['description'] = car.css('.ads-list-detail-item-intro::text').get()
            item['price'] = car.css('.ads-list-detail-item-price::text').get()

        next_page =response.xpath("//*[contains(@class,'current')]/following-sibling::li/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)