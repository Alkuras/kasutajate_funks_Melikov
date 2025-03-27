
from kasutajate_funks_Melikov import *
##1
while True:
   try:
        a=float(input("Arv1: "))
        if a.is_integer():
            break
   except:
       print("Sisesta arv! ")
while True:
    try:
        b=float(input("Arv2: "))
        if b.is_integer():
            break
    except:
        print("Sisesta arv! ")
while True:
    try:
        t=input("Tehe: ")
        if not t.isnumeric():
            break
    except:
        print("Sisesta tehe! ")
vastus=arithmetic(a,b,t)
print(vastus)

#2
aasta=int(input("Mis aassta tahad kontrollida? "))
if aasta>0:
    if is_year_leap(aasta):
        print(f"{aasta} on liigaaasta")
    else:
        print(f"{aasta} ei ole liigaasta")

#3
while True:
    try:
        a=float(input("Ruudu külg= "))
        if a >0 and a.is_integer():
            break
        else:
            print("Sisesta positiivse arvu! ")
    except:
        print("Sisesta positiivse arvu! ")
P,S,d=square(a)
print(P,S,d)


##4
while True:
    try:
        kuu=int(input("Sisesta kuu numbri, kui tahad teada saada mis hooajas ta on "))
        if kuu in range(1,13):
            h=season(kuu)
            break
    except:
        print("Kuud on vahemikus 1-12")
print(f"{kuu}. kuu on hooajas nimega {h}")


#5

while True:
    try:
        euro=float(input("Sisesta kui palku eurot paned pangi "))
        if euro>0:
            break
    except:
        print("Sisesta positiivse arvu ")
while True:
    try:
        aastad=int(input("Sisesta paljuks aastaks paned raha pangi "))
        if aastad>0:
            break
    except:
        print("Sisesta aastade arv!")
vastus=bank(euro,aastad)
print(f"Saad {vastus} eurot")

##6 
while True:
    try:
        arv=int(input("Sisesta arv 0-1000 "))
        prime=is_prime(arv)
        if arv in range(0,1001):
            break
    except:
        print("Sisesta arv 0-1000")
if prime==True:
    print(f"{arv} on lihtne")
else:
    print(f"{arv} ei ole lihtne")

#7
while True:
    try:
        päev=int(input("Sisesta päev "))
        if päev in range(1,32):
            
            break
    except:
        print("Päevad on 1-31")
while True:
    try:
        kuu=int(input("Sisesta kuu "))
        if kuu in range(1,13):
            
            break
    except:
        print("Kuud on 1-12")
while True:
    try:
        aasta=int(input("Sisesta aasta "))
        if aasta >0:
            break
    except:
        print("Aastad algavad 1st")
eks=date(päev,kuu,aasta)
if eks==True:
    print(f"Kuupäev {päev}. {kuu}. {aasta}. eksisteerib")
else:
    print(f"Kuupäev {päev}. {kuu}. {aasta}. ei eksisteeri")



