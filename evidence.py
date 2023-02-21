class Evidence:
    def __init__(self):
        self.jmeno = None
        self.prijmeni = None
        self.stari_osoby = None
        self.tel_cislo = None

        self.pokracovat = True

    @staticmethod
    def nacti_cislo(text_zadani, text_chyba):
        """
        Metoda zkontroluje zadané číslo a v případě nesplnění
        podmínek vypíše chybovou hlášku.
        """
        spatne = True
        while spatne:
            try:
                cislo = int(input(text_zadani))
                spatne = False
            except ValueError:
                print(text_chyba)
            else:
                return cislo

    @staticmethod
    def nacti_text(text_zadani, text_chyba):
        """
        Metoda zkontroluje zadaný text a v případě nesplnění
        podmínek vypíše chybovou hlášku.
        """
        spatne = True
        while spatne:
            text = input(text_zadani)
            if text.isalpha():
                return text
            else:
                print(text_chyba)

    def vyber_akce(self, databaze):
        """
        Metoda umožňuje uživateli vybrat definovanou akci.
        """
        print("------------------------------")
        print("Evidence pojistenych")
        print("------------------------------\n")
        print("Vyberte si akci: ")
        print("1 - Pridat noveho pojisteneho")
        print("2 - Vypsat vsechny pojistene")
        print("3 - Vyhledat pojisteneho")
        print("4 - Konec")
        cislo_akce = self.nacti_cislo("", "Neplatné zadání!")
        if cislo_akce == 1:
            self.pridani_pojisteneho(databaze)
        elif cislo_akce == 2:
            self.vypis(databaze)
        elif cislo_akce == 3:
            self.vyhledavani_pojisteneho(databaze)
        elif cislo_akce == 4:
            self.pokracovat = False
        else:
            print("Neplatná volba!")
            self.vyber_akce(databaze)

    def pridani_pojisteneho(self, databaze):
        """
        Metoda zapisuje nového pojištěnce do databáze.
        """
        self.jmeno = self.nacti_text("Zadejte jmeno pojisteneho: \n", "Jmého nesmí obsahovat čísla ...")
        self.prijmeni = self.nacti_text("Zadejte prijmeni: \n", "Prijmeni nesmí obsahovat čísla ...")
        self.stari_osoby = self.nacti_cislo("Zadejte věk: \n", "Neplatné zadání!")
        self.tel_cislo = self.nacti_cislo("Zadejte telefonni cislo: \n", "Neplatné zadání!")
        databaze.insert_sql(databaze.cur, self.jmeno, self.prijmeni, self.stari_osoby, self.tel_cislo)
        input("\nData byla ulozena. Pokracujte klavesou ENTER ...")

    def vypis(self, databaze):
        """
        Metoda vypisuje seznam všech pojištěnců z databáze.
        """
        databaze.read_sql(databaze.cur)
        input("\nPokracujte klavesou ENTER ...")

    def vyhledavani_pojisteneho(self, databaze):
        """
        Metoda umožňuje vyhledat pojištěnce dle dvou zadaných
        kritérií (jméno, příjmení).
        """
        jmeno = self.nacti_text("Zadejte jmeno pojisteneho: \n", "Jmého nesmí obsahovat čísla ...")
        prijmeni = self.nacti_text("Zadejte prijmeni: \n", "Prijmeni nesmí obsahovat čísla ...")
        databaze.search_sql(databaze.cur, jmeno, prijmeni)
        input("\nPokracujte klavesou ENTER ...")

    def main(self, databaze):
        self.pokracovat = True
        while self.pokracovat:
            self.vyber_akce(databaze)

