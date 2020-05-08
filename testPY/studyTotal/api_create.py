#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import logging
import json

logging.captureWarnings(True)
url='https://ticket.vip.sankuai.com/api/1.0/ticket/fast/create'
headers = {'Accept': 'application/json','content-type': 'application/json','Authorization':'认证','USERNAME':'luoquan04'}
params = {}
#定制请求参数,itemId需要在cti平台创建
params.update(itemId=1231)
params.update(name='测试')
params.update(desc='123')
params.update(ticketType='事件')
params.update(assigned='luoquan04')
params.update(reporter='luoquan04')
params.update(sla='S5')
cc = []
params.update(cc=cc)

r1=requests.post(url=url, data=json.dumps(params), headers=headers, verify=False)
print(r1.text)
