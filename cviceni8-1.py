class Uzivatel:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Uzivatel({self.jmeno}, {self.telefon}, {self.email})"
    @property
    def jmeno(self):
        return self.__jmeno
    @property
    def telefon(self):
        return self.__telefon
    
    @telefon.setter
    def telefon(self, hodnota):
        if len(hodnota) != 13 or hodnota[0] != "+" or not hodnota[1:].isnumeric():
            raise Exception(f"Chybny format cisla: {hodnota}")
        self.__telefon = hodnota
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota or not hodnota.endswith(".cz") or not hodnota.replace("@", "").replace(".", "").isalnum():
            raise Exception(f"Chybny format emailu: {hodnota}")
        self.__email = hodnota
        
    

if __name__ == "__main__":
    u = Uzivatel("Jan", "+420777888999", "jan@novak.cz")
    print(u)


    u.telefon = "+420123456789"
    print(u)

    u.email = "jan.novak@email.cz"
    print(u)
