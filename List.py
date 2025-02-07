L=[]
print(L)
L=list()
print(L)

L=[1,7,9,1,9,6.9,1]
print(L.count(1))

L.append(3)
print(L)
L.extend([5,7,1])
print(L)
L.insert(2,6)
print(L)

L.sort(reverse=True)
print(L)

L.reverse()
print(L)

x=L.pop(2)
print(x)
L.remove(9)
print(L)
L.clear()
print(L)

