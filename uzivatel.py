class Uzivatel:

    def __init__(self, jmeno, heslo, vek):
        self.__jmeno = jmeno
        self.__heslo = heslo
        self.__vek = vek

    def prihlasit(self, heslo):
        ...
    def odhlasit(self):
        ...
    def nastav_vahu(self, zvire):
        ...

        ...

# definice bez dedicnosti
class Administrator:

    def __init__(self, jmeno, heslo, vek, telefonni_cislo):
        self.__jmeno = jmeno
        self.__heslo = heslo
        self.__vek = vek
        self.__telefonni_cislo = telefonni_cislo

    def prihlasit(self, heslo):
        ...
    def odhlasit(self_)
        ...
    def nastav_vahu(self, zvire):
       ...
    def pridej_zvire(self, zvire):
        ...
    def vymaz_zvire(self, zvire):
        ...

        ...

# s pouzitím dedicnosti v zavorce je trida, od ktere se dedi anglicky inheritance
class Administrator(Uzivatel):

    def __init__(self, jmeno, heslo, vek, telefonni_cislo):
    super().__init__(jmeno, heslo, vek)
    self.__telefonni_cislo = telefonni_cislo

    def pridej_zvire(self, zvire):
        ...
    def vymaz_zvire(self, zvire):
        ...

        ...

