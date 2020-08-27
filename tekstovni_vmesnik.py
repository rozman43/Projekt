import model

def izpis_igre(igra):
    return """
        Število napak: {}
        Število pravilnih odgovorov: {}
        Trenutno vprašanje: {}
        """.format(igra.napake(), igra.pravilni(), igra.trenutno_vprasanje)

def izpis_zmage(igra):
    if igra.zmaga():
        return "Čestitke, zmagali ste!"

def izpis_poraza(igra):
    if igra.poraz():
        return "Žal ste izgubili!"

def zahtevaj_vnos():
    odgovor = input("Vpiši odgovor: ")
    return odgovor.lower()

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        odgovor = zahtevaj_vnos()
        rezultat = igra.ugibaj(odgovor)
        if rezultat == model.NI_ODGOVORA:
            print("Prosimo vnesite odgovor!")
            izpis_igre(igra)
        elif rezultat == model.ZMAGA:
            izpis_zmage(igra)
            break
        elif rezultat == model.PORAZ:
            izpis_poraza(igra)
            break
        elif rezultat == model.PRAVILEN_ODGOVOR:
            igra.pravilni_odgovori().append(odgovor)
            igra.naslednje()
            izpis_igre(igra)
        elif rezultat == model.NAPACEN_ODGOVOR:
            igra.napacni_odgovori().append(odgovor)
            igra.naslednje()
            izpis_igre(igra)