def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, int(cislo ** 0,5) + 1):
        if cislo % i == 0:
            return False
    return True