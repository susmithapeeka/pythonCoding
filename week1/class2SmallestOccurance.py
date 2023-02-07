inp1=input('Enter input:')
inp1=list(inp1)
d={}
for ch in inp1:
  d[ch]=d.get(ch,0)+1
min_key=min(d,key=d.get)
min_value=d[min_key]
print(min_key,'has a count of',min_value)
