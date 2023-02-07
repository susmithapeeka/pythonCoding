inp1=input('Enter the input:').lower()
vowels=['a','e','i','o','u']
dic={}
for x in inp1:
  if x in vowels and x not in dic:
    dic[x]=1
  elif x in vowels and x in dic:
    dic[x]+=1
print(dic)
