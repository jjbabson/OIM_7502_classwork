import scrapy

class Sp500PerformanceSpider(scrapy.Spider):
    name = "sp500_performance"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    #Function parse
    def parse(self, response):
        rows = response.xpath('//div[@class="table-responsive"]//table//tbody/tr')

        #row extraction
        #using straing in ytd_return
        #it's giving me an issue with the regular text parse
        for row in rows:
            number = row.xpath('./td[1]/text()').get()
            company = row.xpath('./td[2]/a/text()').get()
            symbol = row.xpath('./td[3]/a/text()').get()
            ytd_return = row.xpath('string(./td[4])').get()

            #also adding more conditionals as this seems related to
            #ytd_return's odd behavior
            if number and company and symbol:
                yield {
                    'rank': number.strip(),
                    'company': company.strip(),
                    'symbol': symbol.strip(),
                    'ytd_return': ytd_return.strip() if ytd_return else None
                }
