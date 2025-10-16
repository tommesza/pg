def my_range(start, stop, step):
    # založení prázdného seznamu
    seznam = []
    cislo = start
    
    # Iterace od start do stop s krokem step
    while cislo < stop:
        # Přidání aktuálního čísla do seznamu
        seznam.append(cislo)
        cislo += step
        
    return seznam
#def for_enumerate(iterable, start=0):
    
    result = []
    
# Pro každý prvek v iterable se přidá index (počítaný od start)
    for index, jmeno in zip(range(start, start + len(iterable)), iterable):
        result.append((index, jmeno))
#range(start, start + len(iterable)) vytvoří řadu čísel začínající od start a dlouhou stejně jako iterable.
#zip spojí tuto řadu s hodnotami v iterable, čímž vytvoří páry (index, hodnota).

#ucitel řešení
def for_enumerate(iterable, start=0):
    result = []

    index = start
    for prvek in iterable:
        result.append((index, prvek))
        index += 1

    return result

def while_enumerate(iterable, start=0):
    result = []  # Vytvoříme prázdný seznam pro uložení výsledků
    index = start  # Počáteční hodnota indexu
    i = 0  # Ukazatel na pozici v iterable (index prvku)

    while i < len(iterable):  # Pokračujeme, dokud neprojdeme celý iterable
        result.append((index, iterable[i]))  # Přidáme dvojici (index, prvek) do seznamu
        index += 1  # Zvýšíme index pro další prvek
        i += 1  # Posuneme ukazatel na další prvek v iterable

    return result  # Vrátíme výsledný seznam








if __name__ == "__main__":

#    text = "abcdef"
#   seznam = ["a", "b", "c", "d", "e", "f"]


    print(list(enumerate(["Alice", "Bob", "Eva"], 1)))
    print(for_enumerate(["Alice", "Bob", "Eva"], 1))
    print(while_enumerate(["Alice", "Bob", "Eva"], 1))


#    print(list(range(1, 10, 2)))
    #zadani parametru do funkce
#    print(my_range(1, 10, 2))

#    index = 0
#    for znak in text:
#        if index % 2 == 0:
#            print(znak)
#       index += 1


#   index = 0
#   while index < len(text):
#       print(text[index])
#        index += 1