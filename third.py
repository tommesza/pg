def je_prvocislo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2): # step = 2 abychom preskocili suda cisla
        if n % i == 0: # pokud n je delitelne i tak neni prvocislo
            return False
    return True
#x

def vrat_prvocisla(maximum):
    prvocisla = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo) == True:
            prvocisla.append(cislo) #kazde prvocislo, ktere "je_prvocislo" detekuje, přidá do seznamu
    return prvocisla


if __name__ == "__main__":
    print(je_prvocislo(1))
    print(je_prvocislo(2))
    print(je_prvocislo(3))
    print(je_prvocislo(100))
    print(je_prvocislo(101))

    print(vrat_prvocisla(1))
    print(vrat_prvocisla(2))
    print(vrat_prvocisla(3))
    print(vrat_prvocisla(10))
