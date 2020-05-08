import requests
param = {'orderNo':'KL19050980600077'}

headers ={'Content-Type':'application/json'}
res1 = requests.get(url='http://10594-qlefj-sl-kladmin.bb.test.sankuai.com/omsapi/self/order/r/detail', params=param, headers=headers)
res2 = requests.post('http://kladmin.bb.test.sankuai.com/oas/self/w/return/afterSalesExcuse/updateStatus', data={'secondExcuseId': '316','valid': '1'})


print(res1.status_code)
print(res2)


