import random
x=(random.randint(0,9))
print(x)
y=(random.randint(0,9))
print(y)
z=int(input("answer by multiplication:"))
if z==int(x)*int(y):
    print("right answer")
else:
    print("worng answer,right answer is:",x*y)
