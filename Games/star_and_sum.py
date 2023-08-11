n = int(input("Please enter a square size "))
if n % 2 == 0:
    n = int(input("Please enter uneven number "))
if n % 2 == 1:
    for i in range(n):
        for j in range(n):
            if ((i == (n-1)/2) and (j != (n-1))) or (i != (n-1)/2 and j == (n-1)/2):
                print("+ ", end=" ")
            elif (i == (n - 1) / 2) and (j == n - 1):
                print("+ ")
            elif (i != (n - 1) / 2) and j !=(n - 1)/2 and j != (n - 1):
                print("* ", end=" ")
            else:
                print("* ")

input("press enter to exit")
