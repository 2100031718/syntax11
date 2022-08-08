#\list1 = [2, 4, 5, 3, 5, 4]
#list2 = [4, 1, 2, 9, 7, 5]
#product = list(map(lambda x, y: x * y, list1, list2))
#print(product)
list1=[1,2,3]
list2=[4,5,6]
products=[a*b for a,b in zip(list1,list2)]
print(products)
