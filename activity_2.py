print(("enter the number you want for rows: "))
n=int(input("enter the number you want for rows: "))
num=1
for i in range(n):
    for j in range(1,i+1):
        print(num, end=" ")
        num = num+1
    print(" ")
    