
# 80-100=A
# 60-79=B
# 50-59=C
# 3O-49=D
# BELOW 30=FAIL
# negative and above 100=invalid input
x=int(input("What is your exam score?"))
if x <= 100 and x>=80:
    print("You got an A")
elif x <= 79 and x>=60:
    print("You got a B")
elif x <= 59 and x>=50:
    print("You got a C")
elif x <=49 and x>=30:
    print("you got a D")
elif x<=30 and x>=0:
    print("FAIL")
else:
    print("invalid input")