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