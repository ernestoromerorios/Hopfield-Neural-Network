import numpy as np
from fractions import Fraction

def patprueb(r1,px,cont):
    for i in range(len(r1)):
        for j in range(len(px)):
            if np.allclose(r1[i],px[j]):
                print(f"Pattern {r1} associates with pattern {px[i]}")
                return True
    for i in range(len(r1)):
        for j in range(len(cont)):
            if np.allclose(r1[i],cont[j]):
                print(f"Pattern {r1} associates with pattern {cont[i]}")
                return True
    return False

m = int(input("Number of patterns (M): "))
n = int(input("Number of neurons (N): "))

cont = []
for i in range (m):
    print(f"\nMatrix {i+1}\n")
    cont.append([])
    for j in range(n):
        x = int(input(f"Data #[{j+1}]: "))
        cont[i].append(x)

print("\nPatterns:\n")
for i in range(m):
    print(f"C{i}: ",end="")
    print("[",end="")
    for j in range(n):
        if j+1 == n:
            print(f"{cont[i][j]}", end="")
        else:
            print(f"{cont[i][j]}", end=",")
    print("]",end="")
    print("\n")

pp = int(input("Number of test patterns (Pp): "))

if (pp > 1):
    px = []
    for i in range(pp):
        print(f"\nPp #{i+1}\n")
        px.append([])
        for j in range(n):
            x = int(input(f"Data #[{j+1}]: "))
            px[i].append(x)
elif pp == 1:
    px = []
    for i in range(n):
        x = int(input(f"Data #[{i+1}]: "))
        px.append(x)

print("\nTest patterns :\n")
if pp > 1:
    for i in range(pp):
        print(f"Pp{i}: ",end="")
        print("[",end="")
        for j in range(n):
            if j+1 == n:
                print(f"{px[i][j]}", end="")
            else:
                print(f"{px[i][j]}", end=",")
        print("]",end="")
        print("\n")
elif pp == 1:
    print("Pp1: [",end="")
    for i in range(n):
        if i+1 == n:
            print(f"{px[i]}", end="")
        else:
            print(f"{px[i]}", end=",")
    print("]",end="")
    print("\n")

pesos = []

for i in range(m):
    pesos.append([])
    for j in range(n):
        for k in range(n):
            pesos[i].append(cont[i][j]*cont[i][k])

pesosfin = []

for j in range(len(pesos[i])):
    pesosfin.append(0)

for i in range(len(pesos)):
    for j in range(len(pesos[i])):
        if i == j:
            pesosfin[j]=pesosfin[j]+pesos[i][j]
        else:
            pesosfin[j]=pesosfin[j]+pesos[i][j]

print("\nWeight Matrix:\n")
pesos.clear()
k = 0
pesos.append([])
for i in range(len(pesosfin)):
    if i+1 == len(pesosfin) or (((i+1)%n) == 0):
        pesos[k].append(pesosfin[i])
    else:
        pesos[k].append(pesosfin[i])
    if ((i+1)%n) == 0:
        k += 1
        if i+1 != len(pesosfin):
            pesos.append([])
for i in range(len(pesos)):
    print("[",end="")
    for j in range(len(pesos[i])):
        if i == j:
            pesos[i][j] = 0
        else:
            pesos[i][j] = pesos[i][j]*(1/n)
        if j+1 == n:
            print(f"{Fraction(str(pesos[i][j])).limit_denominator()}", end="")
        else:
            print(f"{Fraction(str(pesos[i][j])).limit_denominator()}", end=",")
    print("]",end="")
    print("\n")
        
pesos = np.asarray(pesos)

print("\nPatterns iteration:\n")

r1 = []
x = pesos
condicion = True
ciclo = True
bucle = []
cont = np.array(cont)
for i in range(len(cont)):
    print(f"Pattern #{i+1}")
    condicion = True
    x = np.asarray(cont[i])
    while condicion and ciclo:
        r1 = np.dot(pesos,x)
        r1[r1 >= 0] = 1
        r1[r1 < 0] = -1
        print(r1)
        if len(bucle) == 0:
            aux = False
        else:
            aux = np.allclose(np.asarray(r1),np.asarray(bucle))
        if (aux):
            print(f"Infinite core!\n")
            condicion = False
            ciclo = False
        elif (r1 in np.asarray(cont)):
            print(f"Pattern #{i+1} fulfills the condition\n")
            condicion = False
        else:
            print(f"{i+2}° iteration\n")
            bucle.append(x)
            x = r1       

if pp >= 1:
    bucle = []
    ciclo = True
    condicion = True
    x = pesos
    aux = []
    print("\nTest patterns iteration:\n")
    x = np.asarray(px)
    for i in range(pp):
        k = 0
        first = True
        print(f"\nTest patterns iteration #{i+1}")
        bucle = []
        condicion = True
        ciclo = True
        while condicion and ciclo:
            if first:
                r1 = np.dot(pesos,np.transpose(x[i]))
                r1[r1 >= 0] = 1
                r1[r1 < 0] = -1
                first = False
            else:
                r1 = np.dot(pesos,np.array(x))
                r1[r1 >= 0] = 1
                r1[r1 < 0] = -1
            if len(bucle) == 0:
                aux = False
            elif not(aux):
                for j in range(len(bucle)):
                    aux = np.allclose(np.asarray(r1),np.asarray(bucle[j]))
                    if aux:
                        break
            if aux:
                print(f"Infinite core!\n")
                condicion = False
                ciclo = False
            elif patprueb(np.asarray(r1),px,cont):
                print(f"Test pattern #{k+1} fulfills the convergence condition\n")
                condicion = False
            else:   
                print(f"\ny({i})≠y({k+1})\n\n{k+2}° iteration")
                bucle.append(r1)
                x = ""
                x = r1
            k += 1