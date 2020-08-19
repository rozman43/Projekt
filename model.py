# dobiš vprašanja iz datoteke, 2 jih lahko narobe, 5 jih moraš prav da zmagaš

from random import choice
from vprasanja import slovar

STEVILO_DOVOLJENIH_NAPAK = 2
STEVILO_PRAVILNIH = 5
PRAVILEN_ODGOVOR = "+"
NI_ODGOVORA = "0"
NAPACEN_ODGOVOR = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "S"

class Igra:
    def __init__(self, slovar, odgovor=None):
        vprasanje = choice(slovar.keys())
        self.trenutno_vprasanje = vprasanje
        self.pravilen_odgovor = slovar[vprasanje]
        if odgovor == None:
            self.odgovor = []
        else:
            self.odgovor = odgovor

    def napacni_odgovori(self):
        napacni = []
        if self.odgovor != self.pravilen_odgovor:
            napacni.append(self.odgovor)
        return napacni

    def pravilni_odgovori(self):
        pravilni = []
        if self.odgovor == self.pravilen_odgovor:
            pravilni.append(self.odgovor)
        return pravilni

    def napake(self):
        return len(self.napacni_odgovori())

    def pravilni(self):
        return len(self.pravilni_odgovori())

    def zmaga(self):
        self.pravilni() == STEVILO_PRAVILNIH
    
    def poraz(self):
        if self.napake() > STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    def ugibaj(self, odgovor):
        if odgovor == "":
            return NI_ODGOVORA
        elif odgovor == self.pravilen_odgovor:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILEN_ODGOVOR
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACEN_ODGOVOR

def nova_igra():
    return Igra(slovar)

class Kviz:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, odgovor):
        igra = self.igre[id_igre][0]
        stanje = igra.ugibaj(odgovor)
        self.igre[id_igre] = (igra, stanje)