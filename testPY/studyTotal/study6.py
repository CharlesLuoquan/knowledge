l=[]
for i in range(10):
    l.append(str(i))
print(l)
l='aa'.join(l)
print(type(l))

a=l.split("1")
print(a)
origin='http://kladmin.bb.test.sankuai.com/app/afterSale/depositRefund'
path='http://1966-kpqre-sl-kladmin.bb.test.sankuai.com/app/afterSale/depositRefund'
cargo=path.split('//')[1].split('/')[0].split('kladmin')[0]
print(cargo)

url=cargo+origin[7:]
print(url)

c=l.strip('aa')
print(c)

id=1
name='luoquan'
print('no data available for person with id: {}, name: {}'.format(id, name))


kwargs={'a':'luo','b':'quan'}


one='my name is {a} {b}'
print(one.format(**kwargs))
print(kwargs)
print(type(kwargs))
print(kwargs.items())

q='luo'
w='quan'
print('name is {}'.format(q+w))

def table_things(**kwargs):
    for name, value in kwargs.items():
        print ('{0} = {1}'.format(name, value))
table_things(apple = 'fruit', cabbage = 'vegetable')