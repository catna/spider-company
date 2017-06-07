# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class JobuiPipeline(object):
    def process_item(self, item, spider):
        with open('record.csv', 'a') as f:
            fieldnames = ['name', 'size', 'type', 'vocation', 'urlid']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            info_tuple = self.check_size(self.check_text(item['coinfo']))
            writer.writerow({
                'name': self.check_text(item['coname']), 
                'size': info_tuple[0],
                'type': info_tuple[1],
                'vocation': self.check_text(item['vocation']),
                'urlid': item['courlid'][27:-1]
                })

        return item

    def check_text(self, text):
        text = text.replace('\r', '')
        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = text.replace(',', '.')
        text = text.replace(' ', '')
        return text
    
    def check_size(self, text):
        contents = text.split('/')
        cosize = ''
        cotype = ''
        for c in contents:
            if '人' in c:
                cosize = c
            else:
                cotype = c
        return (cosize, cotype)

