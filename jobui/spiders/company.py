# -*- coding: utf-8 -*-
import scrapy
from jobui.items import JobuiItem
import time

class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['jobui.com/company']
    start_urls = ['http://jobui.com/company/']
    url_host = 'http://m.jobui.com/company/'

    def start_requests(self):
        start = 660
        while True:
            str_num = str(start)
            start = start + 1
            yield scrapy.Request(self.url_host + str_num, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = JobuiItem()
        item['coinfo'] = ''
        item['vocation'] = ''

        company_name = response.xpath("//p[@class=\"mb10 fwb fs20\"]/text()")
        company_info = response.xpath("//div[@class=\"mb10 bg-white pd10x15\"]/ul/li")
        
        for li in company_info:
            spans = li.xpath("./span")
            if spans[0].xpath('./text()').extract_first().encode('utf8') == '性质：':
                item['coinfo'] = spans[1].xpath('./text()').extract_first(default='').encode('utf8')
            if spans[0].xpath('./text()').extract_first().encode('utf8') == '行业：':
                item['vocation'] = spans[1].xpath('./text()').extract_first(default='').encode('utf8')
            
        company_vocation = response.xpath("/html/body/section/div[2]/ul/li[2]/span[2]/a/text()")
        
        item['coname'] = company_name.extract_first(default='').encode('utf8')
        item['courlid'] = response.url
        yield item
