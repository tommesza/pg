def vrat_treti(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None
    

def prumer(cisla):
   return sum(cisla) / len(cisla)


def naformatuj_text(student):
    jmeno = student["jmeno"]
    prijmeni = student["prijmeni"]
    vek = student["vek"]
    prumer_znamek = prumer(student["znamky"])
    prumer_znamek = round(prumer_znamek, 2)

    return f"Student: {jmeno} {prijmeni}, Vek: {vek}, Prumer znamek: {prumer_znamek}"


if __name__ == "__main__":
    seznam = [12, 50, 1, 3, 5]
    seznam[3] *= 3
    seznam.append(100)
    seznam.sort()
    seznam.reverse()

    student = {
        "jmeno": "Jan",
        "prijmeni" : "Novak",
        "vek": 22,
        "znamky": [1, 2, 1, 3, 1, 2, 1]
    }
    student["vek"] += 1
     # print(student["znamky"][4])

    print(naformatuj_text(student))
