print(("enter the number you want for rows: "))
n=int(input("enter the number you want for rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")
    