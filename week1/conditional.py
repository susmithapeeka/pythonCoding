def func():
  inp1=input('Enter a number 1: ')
  inp2=input('Enter number 2: ')
  if ord(inp1) in range(48,58) and ord(inp2) in range(48,58):
    print(int(inp1)+int(inp2))
  else:
    func()
func()
