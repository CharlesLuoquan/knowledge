a=[1,2,3,4,5,2,43,41,31,1]
b=[1,2,3,4,5,6,2,1,4,13,1213]

set(a)
set(b)

print(list(set(a) & set(b)))

print(set(a) ^ set(b))

kb_order="orderNo=KB19112550600030"
kb_order = kb_order.split("=")[1][:-1]
print(kb_order)