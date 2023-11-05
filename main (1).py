#Implement a recursive function to calculate the factorial of a given number.
def recurfactorial(n):
 if n==1:
  return n
 else:
  return n*recurfactorial(n-1)
#take input from the user.
num=int(input("Enter a number :"))
#check is the number us negative.
if num<0:
  print ("Sorry, factorial does not exist for negative numbers ")
elif num == 0:
  print ("The factorial of 0 is 1")
else:
  print ("The factorial of",num,"is",recurfactorial (num))