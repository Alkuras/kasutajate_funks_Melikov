from math import *
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Kui sisend ei ole jarjendis[+,-,/,*], siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarvu tüübina
    :param float arv2: Sisend ujukomaarvu tüübina
    :param str tehe: Sisend listis [+,-,/,*]
    :rtype: var Määramate tüüp (float või str)
    """
    if tehe in ["+","-","/","*"]:
        if arv2==0 and tehe=="/":
            vastus="!DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(year:int)-> bool:
    """Liigaasta tuvastaja
    Sisesta aastat ja saad kas ligaasta või tavaline aasta
    :param int year: Sisend aasta int tüübina
    :rtype: bool 
    """
    if year%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def square(square_side:float)-> any:
    """Arvutab ruudu ümbermõõt,läbimõõt ja diagonaal

    :param float square_side: Sisend ujukomaarvu tüübina
    :rtype: var funktsioon tagastab kolm arvu: P, S, d
    """

    if square_side>0:
        P=square_side*4
        S=square_side**2
        d=square_side*sqrt(2)
    else:
        print("Arv peab olema positiivne")
    return P,S,d
    return S
    return d

def season(month:int)-> str:
    """Kirjutab millele hooajale kulub sisestatud kuu
    
    :param int month: Sisend 1-12 täisarvu tüübina
    :rtype: str funktsioon tagastab vastust tekstina
    """
    talv=[12,1,2]
    kevad=[3,4,5]
    suvi=[6,7,8]
    sügis=[9,10,11]
    if month in talv:
        vastus="Talv"
    elif month in kevad:
        vastus="Kevad"
    elif month in suvi:
        vastus="Suvi"
    elif month in sügis:
        vastus="Sügis"
    else:
        print("Viga!")
    return vastus

def bank(summ:float,years:int)->float:
    """Kirjutab palju raha saad pangist

    :param float summ: palju eurot pangasse
    :param int years: paljuks aastaks paned raha
    :rtype: float funktsioon tagastab palju raha lõppuks saad
    """
 
    for aasta in range(years):
   

        summ*=1.1
    return summ
        

def is_prime(arv:int)->bool:
    """Tagastab True, kui arv on lihtne
    False, kui mitte
    :param int arv: arv mida tahad kontrollida
    :rtype: bool funktsioon tagastab True, kui arv on lihtne
    """
 
    if arv <=1:
        return False
    for i in range(2,arv):
        if arv%i==0:
            return False
        return True
           

def date(day:int,month:int,year:int)->bool:
    """Funktsioon kontrollib kas on sisestatud kuupäev meie kalendris või mitte
    :param int day: päev täisarv tüübina
    :param int month: kuu täisarv tüübina
    :param int year: aasta täisarv tüübina
    :rtype: bool funktsioon tagastab True, kui sisestatud kuupäev eksisteerib ja False, kui ei eksisteeri
    """
    v=False
    if month in range(1,13) and year >0:
        if month in [1,3,5,7,8,10,12]:
            if day in range(1,32):
                v=True
        if month in [4,6,9,11]:
            if day in range(1,31):
                v=True
        if month==2:
            if is_year_leap(year):
                if day in range(1,30):
                    v=True
            elif not is_year_leap(year):
                if day in range(1,29):
                    v=True
       
    return v

def average(arvud:list)->any:
    """Võtab argumendiks järjendi arvudega ja tagastab nende aritmeetilise keskmise.
    :param list arvud: arvud listis
    :rtype: any
    """
    if len(arvud)==0:
        return None
    else:
        summ=sum(arvud)/len(arvud)
        return summ 
                