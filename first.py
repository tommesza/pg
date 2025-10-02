def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print(f"Cislo {cislo} je sude")
    else:
        print(f"Cislo {cislo} je liche")

if __name__ == "__main__":
    cislo = input("Zadej cislo: ")
    cislo = int(cislo)
    
    sudy_nebo_lichy(cislo)
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)