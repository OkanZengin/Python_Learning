import random

command = "xyz"
while command != "bye":
    y = input("aralık başlangıç noktası seçiniz ")
    t = input("aralık bitiş noktası seçiniz ")
    x = random.randint(int(y), int(t))
    gss = input(f"{int(y)} ile {int(t)} arasında ( {int(y)} , {int(t)} ) dahil tuttuğum sayıyı bul ")
    syc = 1
    while syc < 10000:
        if int(gss) == x:
            print(f"tebrikler. sayıyı buldun. Hem de {syc} tahminde")
            break
        if int(gss) != x:
            if int(gss) < x:
                gss = input("yukarı: ")
            if int(gss) > x:
                gss = input("aşağı: ")
            syc += 1
        if syc == (int(t) - int(y) + 2):
            print(" sayıyı bulamadın :( ")
            break
    command = input("type 'bye' to exit or press 'enter' to go again ").lower()
input("press enter to exit")
