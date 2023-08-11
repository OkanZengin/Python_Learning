result=1
command="asd"
while command!="bye":
    command = input("Please enter the number you want to have the factory! or type 'bye' to exit ").lower()
    if command=="bye":
        break
    else:
        i = int(command)
        if i>0:
            while i > 0:
                result = result * i
                i-=1
            print(result)
            result=1
        else:
            print(result)
print("BYE")