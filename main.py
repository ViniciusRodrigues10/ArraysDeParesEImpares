def ParOuImpar(valor):
    if valor % 2 == 0:
        return "par"
    else:
        return "impar"


par = []
impar = []
for i in range(15):

    valor = int(input())
    if ParOuImpar(valor) == "par":
        if len(par) < 5:
            par.append(valor)
        else:
            for i in range(len(par)):
                print(f"par[{i}] =", par[i])
            par = []
            par.append(valor)

    elif ParOuImpar(valor) == "impar":
        if len(impar) < 5:
            impar.append(valor)
        else:
            for i in range(len(impar)):
                print(f"impar[{i}] =", impar[i])
            impar = []
            impar.append(valor)

for i in range(len(impar)):
    print(f"impar[{i}] =", impar[i])

for i in range(len(par)):
    print(f"par[{i}] =", par[i])
