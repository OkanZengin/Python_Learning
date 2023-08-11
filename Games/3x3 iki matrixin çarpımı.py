print("elemanları istenen 3x3 iki matrixin çarpımı")
command = input("çıkmak için 'bye' yazın, devam etmek için 'devam' yazın ").lower()
while True:
    if command=="bye":
        print("BYE")
        break
    elif command=="devam":
        asd=[]
        bsd=[]
        for x in range(3):
            matrix=[]
            for y in range(3):
                matrix.append(int(input(f"Lütfen 1.matrix {x+1}.satır {y+1}.sütun elemanını giriniz ")))
            asd.append(matrix)

        for x in range(3):
            matrix_k=[]
            for y in range(3):
                matrix_k.append(int(input(f"Lütfen 2.matrix {x+1}.satır {y+1}.sütun elemanını giriniz ")))
            bsd.append(matrix_k)
        print("1.matrix")
        for g in range(3):
            print(asd[g])
        print("2.matrix")
        for f in range(3):
            print(bsd[f])
        multiply_matrix=[[],[],[]]
        multiply_matrix=[
            [((asd[0][0]*bsd[0][0])+(asd[0][1]*bsd[1][0])+(asd[0][2]*bsd[2][0])),((asd[0][0]*bsd[0][1])+(asd[0][1]*bsd[1][1])+(asd[0][2]*bsd[2][1])),((asd[0][0]*bsd[0][2])+(asd[0][1]*bsd[1][2])+(asd[0][2]*bsd[2][2]))],
            [((asd[1][0]*bsd[0][0])+(asd[1][1]*bsd[1][0])+(asd[1][2]*bsd[2][0])),((asd[1][0]*bsd[0][1])+(asd[1][1]*bsd[1][1])+(asd[1][2]*bsd[2][1])),((asd[1][0]*bsd[0][2])+(asd[1][1]*bsd[1][2])+(asd[1][2]*bsd[2][2]))],
            [((asd[2][0]*bsd[0][0])+(asd[2][1]*bsd[1][0])+(asd[2][2]*bsd[2][0])),((asd[2][0]*bsd[0][1])+(asd[2][1]*bsd[1][1])+(asd[2][2]*bsd[2][1])),((asd[2][0]*bsd[0][2])+(asd[2][1]*bsd[1][2])+(asd[2][2]*bsd[2][2]))]
        ]
        print("multiplied matrix is ")
        for x in range(3):
            print(multiply_matrix[x])
        command=input("çıkmak için 'bye' yazın, devam etmek için 'devam' yazın ").lower()
    elif command!="bye" or "devam":
        command=input("Anlamadım :/ ")
input("press enter to exit")