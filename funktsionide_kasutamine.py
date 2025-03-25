
from kasutajate_funks_Melikov import *

a=float(input("Arv1: "))
b=float(input("Arv2: "))
t=input("Tehe: ")
vastus=arithmetic(a,b,t)
print(vastus)


aasta=int(input("Mis aassta tahad kontrollida? "))
if aasta>0:
    if is_year_leap(aasta):
        print(f"{aasta} on liigaaasta")
    else:
        print(f"{aasta} ei ole liigaasta")


