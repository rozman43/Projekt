
from vprasanja import slovar
import random 

STEVILO_DOVOLJENIH_NAPAK = 2
STEVILO_PRAVILNIH = 5
PRAVILEN_ODGOVOR = "+"
NI_ODGOVORA = "0"
NAPACEN_ODGOVOR = "-"
ZMAGA = "W"
PORAZ = "X"
ZACETEK = "S"


class Igra:
    def __init__(self, stevilo_vprasanj):
        "Prvo smo slovar spremenili v seznam. Potem pa nam sample vrne seznam (stevilo_vprasanj) toliko vprasanj iz seznama vprasanj"
        self.vprasanja = random.sample(list(slovar), stevilo_vprasanj)
        self.pravileni_odgovori = 0
        self.st_trenutnega_vprasanja = 0
    
    def st_pravilni_odgovori(self): 
        "vrne stevilo pravilnih odgovorov"
        return self.pravileni_odgovori
    
    def st_napacni_odgovori(self):
        "vrne stevilo napacnih odgovorov"
        return self.st_trenutnega_vprasanja - self.pravileni_odgovori
    
    def trenutno_vprasanje(self):
        "vrne trenutno vprasanje"
        return self.vprasanja[self.st_trenutnega_vprasanja]

    def poraz(self):
        return self.st_napacni_odgovori() > STEVILO_DOVOLJENIH_NAPAK
    
    def zmaga(self):
        return self.pravileni_odgovori >= STEVILO_PRAVILNIH 


    def ugibaj(self, odgovor):
        "metoda ugibaj preveri igralcev odgovor, pri tem pa poveca st trenutnega vprasanja za +1"
        if odgovor == "":
            return NI_ODGOVORA
        pravilni_odgovor = slovar[self.trenutno_vprasanje()]
        self.st_trenutnega_vprasanja += 1
        if odgovor == pravilni_odgovor:
            self.pravileni_odgovori += 1
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
    return Igra(STEVILO_PRAVILNIH + STEVILO_DOVOLJENIH_NAPAK)

class Matquiz:
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