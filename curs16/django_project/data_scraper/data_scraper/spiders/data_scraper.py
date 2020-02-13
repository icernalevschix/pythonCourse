import scrapy
from data_scraper.items import PostItem
from django.contrib.auth.models import User

class JobsSpider(scrapy.Spider):
    name = 'jobs'

    def start_requests(self):
        url = 'https://www.rabota.md/ro/vacancies/category/it'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for job in response.css('.vacancy-block'):
            item = PostItem()
            item['title'] = job.css('.vacancy-block__name::text').get()
            # item['author'] = job.css('.vacancy-block__company-name span::text').get()
            item['author'] = User(id=1)
            item['content'] = job.css('.vacancy-block__requirements::text').get().strip().replace('\r\n', '')
            item['sallary'] = job.css('.vacancy-block__salary::text').get().strip()
            yield item