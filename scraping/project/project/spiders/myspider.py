import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.data.jma.go.jp']
    start_urls = ['https://www.data.jma.go.jp/svd/eqev/data/daily_map/20220430.html']

    def parse(self, response):
        # eqlist = response.xpath('//h1')
        # yield {
        #     'eqlist': eqlist.xpath('./text()').get()
        # }

        # eqlist = response.xpath('//ul[text()=震源リスト]/li/ul')
        # yield {
        #     # 'eqlist': eqlist.xpath('.//pre/text()').get()
        #     'eqlist': eqlist.xpath('./pre/text()').get()
        # }

        eqlist = response.xpath('//li/ul')
        yield {
            # 'eqlist': eqlist.xpath('.//pre/text()').get()
            'eqlist': eqlist.xpath('./pre/text()').get()
        }

        # pass
