# if...else..else statement
# create a program for grades input with the following
# 80-100=A
# 60-79=B
# 50-59=C
# 3O-49=D
# BELOW 30=FAIL
# negative and above 100=invalid input
num=int(input("enter the first number"))
num2=int(input("enter second number"))
num3=int(input("enter the third numer"))
num4=int(input("enter the fourth numer"))

if num>num2 and num>num3 and num>num4:
    print(num,"is greater")
elif num2>num and num2>num3 and num2>num4:
    print(num2,"is greater")
elif num3>num and num3>num2 and num3>num4:
    print(num3,"is greater")
elif num4>num and num4>num3 and num4>num2:
    print(num4,"is greater")
else:
    print("number invalid")