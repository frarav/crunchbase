from scrapy.spider import BaseSpider

class CrunchSpider(BaseSpider):
    name = "crunch"
    allowed_domains = ["cbasewrap.ontologycentral.com"]
    start_urls = [
        "http://cbasewrap.ontologycentral.com/company/"
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)