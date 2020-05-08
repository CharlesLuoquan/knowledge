import json

params={
    'id':1,
    'name':'luoquan',
    'love':'huiying'
}
print(params)
str=json.dumps(params)

print(str)

origin=json.loads(str)
print(origin)

l=[1,2,'22','luo']
strl=json.dumps(l)
print(strl)
print(type(strl))
print(json.loads(strl))
print(type(json.loads(strl)))

a=[1,2,"1"]
print(type(a))
c=json.dumps(a)
print(type(c))
b=json.loads(c)
print(type(b))


with open('a.json','w') as fn:
    a_str=json.dump(params,fn)
with open('ab.json','w') as fn:
    fn.write('{"id":1}')

with open('ab.json','r') as fin:
    abcd=json.load(fin)
print(abcd)
print(type(abcd))