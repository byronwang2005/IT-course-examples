gs=0
for i in range(100,1000):
    g=i%10
    s=i//10%10
    b=i//100
    if g**3+s**3+b**3==i:
        print(i," ")
        gs+=1
print("有水仙花数",gs,"个")
input("") #防止程序直接退出