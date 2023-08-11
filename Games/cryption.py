alphabet = [
    "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş",
    "T", "U", "Ü", "V", "Y", "Z", "W"," ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", ";", "?", "(",
    ")"]
numbers = [4, 2, 7, 5, 1, 23, 6, 324, 456, 234, 545, 445, 34, 54, 67, 678, 780, 80, 57, 45, 345, 56, 89, 90, 3, 356, 44,
           85, 95, 754, 1010, 98, 13, 32, 41, 515, 71, 73, 15, 21, 112, 9, 11, 22, 33, 49, 55, 66]
message = input("input message ").upper()
msg = []
crypt = []
i = 0
for a in message:
    msg.append(a)
n = len(msg)
while i < n:
    k = msg[i]
    t = alphabet.index(k)
    crypt.append(numbers[t])
    i += 1
print(crypt)
input("press enter to exit")
