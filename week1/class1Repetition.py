#Take a string from user and incase if you find any repitition then remove both characters and return strings
         
inp1=input()
j=""
# hrl
for x in range(len(inp1)-1):
  if inp1[x]==inp1[x+1] or inp1[x-1]==inp1[x]:
    continue
  else:
    j+=inp1[x]
x+=1
if inp1[x]!=inp1[x-1]:
  j+=inp1[x]
print(j)
