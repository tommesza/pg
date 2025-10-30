import sys
import csv

def nacti_csv(soubor):
    data = []
    fp = open(soubor)
    reader = csv.reader(fp)
    for row in reader:
        data.append(row)
    fp.close()
    return data


def spoj_data(data1, data2):
    head1 = data1[0]
    head2 = data2[0]
    data1 = data1[1:]
    data2 = data2[1:]

    # head = set(head1)
    # head.update(head2)
    head = list(dict.fromkeys(head1 + head2))

    data = {}
    for row in data1:
        jmeno_prijmeni = (row[0], row[1])
        data[jmeno_prijmeni] = {}
        for k,v in zip(head1, row):
            data[jmeno_prijmeni][k] = v
    for row in data2:
        jmeno_prijmeni2 = (row[0], row[1])
        if jmeno_prijmeni not in data:
            data[jmeno_prijmeni2] = {}
        for k,v in zip(head2, row):
            data[jmeno_prijmeni2][k] = v
    for v in data.values():
        for h in head:
            print(f"{h} = {v.get}")




print(data)



def zapis_csv(soubor, data):
    with open(soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        print(csv_data1)
        print(csv_data2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Nebyly zadany soubory")
    except FileNotFoundError:
        print("Soubor neexistuje")