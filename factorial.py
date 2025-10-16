def faktorial(cislo):
    if cislo == 0 or cislo == 1:
        return 1
    return cislo * faktorial(cislo - 1)
    

def faktorial2(cislo):
    if cislo == 0:
        return 1
    vysledek = 1  
    for n in range(2, cislo + 1):
        vysledek *= n
    return vysledek



if __name__ == "__main__":
    print(faktorial(0))
    print(faktorial(1))
    print(faktorial(5))
    print(faktorial(10))

    print(faktorial2(0))
    print(faktorial2(1))
    print(faktorial2(5))
    print(faktorial2(10))