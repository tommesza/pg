def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdálenost říká, jak jsou 2 řetězce rozdílné, pokud jsou stejné, vzdálenost je 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdálenost 1 (liší se v 1 písmenu)
    """
    i = 0
    levenstein = 0
    lenght = min(len(dotaz1), len(dotaz2))
    while i < lenght:
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
        i += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))

    return levenstein



def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    lenght = min(len(dotaz1), len(dotaz2)) # délka kratšího řetězce
    levenstein = 0
    for i in range(lenght): 
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2)) # přičteme rozdíl v délce řetězců
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost_for(query1, query2)) #2
    print(levensteinova_vzdalenost_for(query2, query3)) #3
    print(levensteinova_vzdalenost_for(query1, query3)) #1
    print(levensteinova_vzdalenost_for(query1, query4)) #0
    print("----")

    print(levensteinova_vzdalenost(query1, query2)) #2
    print(levensteinova_vzdalenost(query2, query3)) #3
    print(levensteinova_vzdalenost(query1, query3)) #1
    print(levensteinova_vzdalenost(query1, query4)) #0