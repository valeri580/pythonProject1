import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div.lsooF')
        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.q5Uds span::text').get(),
                'url': svet.css('a').attrib['href']
            }


