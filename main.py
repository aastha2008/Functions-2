# get Name function
'''
def getName():
  userName = input("Please tell me your name: ")
  return userName
  
def greetUser(name): #parameter variable are specific to the function
  print("Hi " + name)

name1 = getName()
print("name 1 is" + name1)

greetUser(name1)

#name2 = getName()
#greetUser(name2)

#name3 = getName()
#greetUser(name3)


# write a function that takes num1 and num2 as parameters
# print the sum
def addition(a, b):
    sum = a + b
    return sum


#ask the user for two numbers
# num1
# num2
userNum1 = int(input("Please enter your first number: "))
userNum2 = int(input("Please enter your second number: "))
x = addition(userNum1, userNum2)
print(x)


# write a function that takes num1 and num2 as parameters 
# print the sum

z = 5
x = [3,2,5,6]
print("first x is:" + str(x))
x = sum([3,2,5,6]) 
print("x is:" + str(x))
y = sum([4,6,7,8,4,6,7,8,9,0,7])

def multiply(c,d):
  product = c * d
  return product
  


userNum1 = int(input("Please enter your first number: "))
userNum2 = int(input("Please enter your second number: "))

x = multiply(userNum1, userNum2)
print(x)

def names(x,y):
  #print(str(x) + " is the best friend of " + str(y))
  friends = (str(x) + " is the best friend of " + str(y))
  return friends
  
  
n1= input("Please enter your first name: ")
n2= input("Please enter your second name: ")
#names(n1,n2)
a=names(n1, n2)
print(a)
''' 
#Do the function
def subtraction(x,y):
  difference = x-y
  return difference

#Get two numbers from the user
num1= int(input("What is your first number: "))
num2= int(input("What is your second number: "))

#Call the function
a=subtraction(num1, num2)
print("The difference between your numbers is " + str(a))

#Do the if statements based off of your answer
if(a < 0):
  print("Your first number was less than your second number")

elif(a>0):
  print("Your first number was greater than your second number")

else:
  print("Your first number was the same as your second number")
