import scrapy

class FccSpider(scrapy.Spider):
    name = "fcc"
    allowed_domains = ["fccid.io"]
    start_urls = ["https://fccid.io/UXD/example"]

    def parse(self, response):
        title = response.css("title::text").get()
        yield {
            "url": response.url,
            "title": title.strip() if title else None,
        }

        for href in response.css('a::attr(href)').getall():
            if href.startswith('/UXD') and href.endswith('/example'):
                yield response.follow(href, self.parse)
