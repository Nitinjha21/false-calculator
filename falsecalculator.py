# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print("Type number 1:")
num1=int(input())
print("Type number 2:")
num2=int(input())
print("select the operations"'+,-,*,/,%,')
num3=input()
if num1==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1==56 and num2==6 and num3=='/':
    print("4")
elif num3=='+':
    plus=num2+num1
    print(plus)
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3=='/' :
    dev=num2/num1
    print(dev)
elif num3== '-':
    dev=num2-num1
    print(dev)
elif num3=='%' :
    percent=num2%num1
    print(percent)
else :
    print("error! check your input.")
            
    
    
                