def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """

    typ = figurka["typ"]
    sr, ss = figurka["pozice"] # startovní řádek a sloupec
    cr, cs = cilova_pozice # cílový řádek a sloupec

    # 1) Kontrola, zda je cílová pozice uvnitř šachovnice
    if not (1 <= cr <= 8 and 1 <= cs <= 8):
        return False

    # 2) Cílové pole musí být volné
    if cilova_pozice in obsazene_pozice:
        return False

    rr = cr - sr #rozdíl řádků
    rs = cs - ss #rozdíl sloupců
    abs_rr = abs(rr) #absolutní hodnota aby to nebylo minus
    abs_rs = abs(rs)

    # Pomocná funkce: zkontroluje, že cesta je volná
    def cesta_volna():
        # Ověří, že mezi startem a cílem nestojí jiná figura
        if rr != 0: #rozdil nesmi byt nula (deleni nulou)
            step_r = (rr // abs_rr)
        else:
            step_r = 0
        if rs != 0:
            step_s = (rs // abs_rs)
        else:
            step_s = 0
        r = sr + step_r
        s = ss + step_s
        while (r, s) != (cr, cs):
            if (r, s) in obsazene_pozice:
                return False
            r += step_r
            s += step_s
        return True

    # --- Logika pro jednotlivé figury ---

    if typ == "pěšec":
        # Pěšec se může pohnout pouze o jedno pole dopředu (směr = vyšší řádek)
        if rs != 0:
            return False  # pěšec nejde do boku
        if rr == 1 and (cr, cs) not in obsazene_pozice:
            return True
        # dvě pole vpřed jen z prvního řádku
        if sr == 1 and rr == 2:
            stred = (sr + 1, ss)
            return (stred not in obsazene_pozice) and (cilova_pozice not in obsazene_pozice)
        return False

    elif typ == "jezdec":
        # cesta nemusi byt volna
        return (abs_rr == 2 and abs_rs == 1) or (abs_rr == 1 and abs_rs == 2)

    elif typ == "věž":
        # pohyb v řadě nebo sloupci
        if rr == 0 or rs == 0:
            return cesta_volna()
        return False

    elif typ == "střelec":
        # diagonální pohyb
        if abs_rr == abs_rs:
            return cesta_volna()
        return False

    elif typ == "dáma":
        # kombinuje pohyb věže a střelce
        if rr == 0 or rs == 0 or abs_rr == abs_rs:
            return cesta_volna()
        return False

    elif typ == "král":
        # o jedno pole všemi směry
        return max(abs_rr, abs_rs) == 1



if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
    print("---")
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False
    print("---")
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
