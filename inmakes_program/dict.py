x= {'name':"kukku",'age':21,'school':'abc'}
print(x['name'])
print(x.keys())
print(x.items())
print(x.values())

y = x.get("name")
print(y)

x['name']="bhavana"
print(x)

x.update({'name':"chinnu"})
print(x)


x.popitem()
x.pop("name")
print(x)

y= {'name':"kukku",'age':21,'school':'abc'}
for i in y.keys():
    print(i)

movie = {1:{'name':"nandanam","date":2000},2:{'name':'billale','date':2011}}
print(movie)