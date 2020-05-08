import json
raw_data=[{"csuCode": 10080336, 'skuCode': 10019087, 'goodsId': 10080336, 'quantity': 3, 'goodsType': 1, 'name': '订单自动化-满减商品', 'ssuName': '订单自动化-满减商品', 'brands': '华美', 'salesPrice': 50}]
json_raw_data=json.dumps(raw_data)
print(json_raw_data)
print(type(json_raw_data))

a='luoquan11@@das@#@！¥@#'
print(type(a))
try:
    data = json.loads(a)
    print(type(data))
    print(data)
except json.JSONDecodeError as err:
    print('JSONDecodeError: {}'.format(err))
# except:
#     print('other error')
