import scrapy


class Srpages2Spider(scrapy.Spider):
    name = 'srPages2'
    allowed_domains = ['www.sreality.cz']
    # start_urls = ['https://www.sreality.cz/en/search/for-sale/apartments?strana=3&_escaped_fragment_=']
    start_urls = ["https://www.sreality.cz/en/search/for-sale/apartments?strana=%d&_escaped_fragment_=" % i for i in range(1,2)]
    def parse(self, response):
        apartments = response.xpath('//*[@class="property ng-scope"]')
        # address={}
        title={}
        imgSrc={}
        count = 0
        for apartment in apartments:
            count += count
            # address[count] = apartment.xpath('.//*[@class="locality ng-binding"]/text()').get()
            title[count]   = apartment.xpath('.//*[@class="title"]/*[@class="name ng-binding"]/text()').get()
            imgSrc[count]   = apartment.xpath('.//*[@class="ng-scope ng-isolate-scope"]/*[@class="_15Md1MuBeW62jbm5iL0XqR _1sm7uHIebD7tngzBEQy3dD"]/*[@class="_2xzMRvpz7TDA2twKCXTS4R"]/a[2]/img/@src').get()
           
            yield {
                'title'  : title[count],
                'img_src'  : imgSrc[count],
                # 'address': address[count]
                }
    