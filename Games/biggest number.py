x=0
y=0
big=0
t=0
n=int(input("Please type list size "))
list=[]
while x<n:
    t=int(input(f"input number {x+1} to the list "))
    list.append(t)
    x+=1
x=0
for x in range(n):
        if big <= list[x]:
            big=list[x]
            y=x
        else:
            x+=1
print(f"biggest number in the list is {big} and index is {y}")
input("press enter to exit")