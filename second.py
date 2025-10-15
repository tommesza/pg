def cislo_text(cislo):
    # Pokud je číslo předáno jako text, převedeme ho na int
    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři",
                 "pět", "šest", "sedm", "osm", "devět"]
# prvni prázdná protože se počítá od nuly (jinak by "1." bylo dvacet)
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet",
                "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    # 11–19
    nact = {
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct"
    }
# mensi nez 10
    if cislo < 10:
        return jednotky[cislo]
# 10-19
    elif 10 < cislo < 20:
        return nact[cislo]
# 20 - 99
    elif 20 <= cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + jednotky[jednotka]
# 10
    elif cislo == 10:
        return "deset"
# 100
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah (0–100)"


if __name__ == "__main__":
    cislo = input(f"Zadej číslo 0-100: ")
    print(f"{cislo} -> {cislo_text(cislo)}")