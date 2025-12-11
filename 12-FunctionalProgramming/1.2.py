# takes two numbers from keyboard
n1 = int(input("Put in the first number: "))
n2 = int(input("Put in the second number: "))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")