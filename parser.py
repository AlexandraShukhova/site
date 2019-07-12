#!/usr/bin/env python
# coding: utf-8


import scrapy
import requests # для запросов к сайту
import pandas as pd # для обработки и сохранения данных
import random # для случайных запросов

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process, Queue
from twisted.internet import reactor

from mur.items import MurItem

import json

# муркоша
class Murkosha(scrapy.Spider):
    name='murkosha'

    start_urls=['https://murkosha.ru/pokazat-vsekh/']

    def parse(self, response):
        item = MurItem()
        
        SET_SELECTOR='//div[@class="itemContainer"]'
        for i in response.xpath(SET_SELECTOR):
            item['photo'] = i.xpath('.//div[@class="catItemImageBlock"]/a/@href').get()
            item['name'] = i.xpath('.//div[@class="blog-item-title"]/a/text()').extract_first().strip()
            item['gender'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeMultipleSelect grouppol"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['age'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="even typeTextfield groupVozpast"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['lotok'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupznaetlotok"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['vetpasport'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupvetpassport"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            yield item
            continue
            yield {
                'photo':i.xpath('.//div[@class="catItemImageBlock"]/a/@href').get(),
                'name':i.xpath('.//div[@class="blog-item-title"]/a/text()').extract_first().strip().encode('utf-8'),
                'gender':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeMultipleSelect grouppol"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'year':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="even typeTextfield groupVozpast"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'lotok':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupznaetlotok"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'vetpasport':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupvetpassport"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
            }
        SET_SELECTOR='//div[@class="itemContainer itemContainerLast"]'
        for i in response.xpath(SET_SELECTOR):
            item['photo'] = i.xpath('.//div[@class="catItemImageBlock"]/a/@href').get()
            item['name'] = i.xpath('.//div[@class="blog-item-title"]/a/text()').extract_first().strip()
            item['gender'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeMultipleSelect grouppol"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['age'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="even typeTextfield groupVozpast"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['lotok'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupznaetlotok"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            item['vetpasport'] = i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupvetpassport"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '')
            yield item
            continue
            yield {
                'photo':i.xpath('.//div[@class="catItemImageBlock"]/a/@href').get(),
                'name':i.xpath('.//div[@class="blog-item-title"]/a/text()').extract_first().strip().encode('utf-8'),
                'gender':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeMultipleSelect grouppol"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'year':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="even typeTextfield groupVozpast"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'lotok':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupznaetlotok"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
                'vetpasport':i.xpath('.//div[@class="itemExtraFields"]/ul[@class="charlist dd2"]/li[@class="odd typeRadio groupvetpassport"]/span[@class="itemExtraFieldsLabel"]/text()').extract_first().strip().replace('\t', '').replace('\n', '').encode('utf-8'),
            }
        NEXT_PAGE='//div[@class="wr"]/div[@class="topchik"]/div[@class="post"]/div[@class="clategory itemListView pokazat_vseh hide_extra"]/div[@class="k2Pagination"]/ul/li[@class="pagination-next"]/a/@href'
        next_page=response.xpath(NEXT_PAGE).get()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),callback=self.parse
            )
        #self.parse



