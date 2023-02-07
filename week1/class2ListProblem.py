list1=[12,34,76,'hh',90.8,76.9,"ABC"]
l2=[]
for x in range(len(list1)):
  if type(list1[x])==int:
    l2.append(list1[x]**2)
  elif type(list1)==str:
    pass
  elif type(list1)==float:
    l2.append(list1[x])
print(l2)
