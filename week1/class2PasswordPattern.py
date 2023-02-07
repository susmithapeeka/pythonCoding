''' Take an input from user and check the data based on the following conditions

data should be string data type
The length of input should lie in the range from 6 to 15 characters
Input should have atleast one capital letter(A-J)
One small letter(a-j)
One number from 1-9
One special character ( # @ $ %)
If any of condition is not valid ask for the input from the user upto 4 times otherwise exit the program by putting a message input give is wrong'''


def function(inputs,counts):
  numeric=0
  upper=0
  lower=0
  special=0
  flag=False
  while(flag==False and counts<5):
    for x in inputs:
      if ord(x) in range(48,58):
        numeric+=1
      if ord(x) in range(65,74):
        upper+=1
      if ord(x) in range(97,106):
        lower+=1
      if ord(x)==35 or ord(x)==64 or ord(x)==36 or ord(x)==37:
        special+=1
    if(numeric>=1 and upper>=1 and lower>=1 and special>=1 and len(inputs) in range(6,16) and type(inputs)==str):
      return "Successful"
    else:
      inputs=input("Enter input again:")
      counts+=1
  return "Fail"



function("Abc1239",0)

