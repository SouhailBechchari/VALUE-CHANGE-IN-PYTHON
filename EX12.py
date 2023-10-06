A = int(input("tapez le premier entier :"))
B = int(input("tapez le deuxieme entier :"))
C = A
if A * B > 0 :
    A = B
    B = C
    print("la valeur de A est :", A, "la valeur de B est :", B)
else :
    A = A + B
    B = C * B
    print("la somme :", A, "la multiplication :", B)  