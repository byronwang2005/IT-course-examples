num=int(input())
m={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
for i in range(100,1000):
    g=i%10
    s=i//10%10
    b=i//100
    z=m[g]+m[s]+m[b]
    if z==num:
        print(i)
input("回车退出程序")